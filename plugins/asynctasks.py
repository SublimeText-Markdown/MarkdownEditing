# Adapted from https://github.com/jisaacks/GitGutter

import functools
import threading

import traceback

from queue import Empty
from queue import Queue
from threading import Thread


class PromiseError(Exception):
    """A failed Promise is to be resolved with this PromiseError.
    Normal errors and exceptions can't be catched by the applicaiton due to
    multithreading. Therefore a function should return PromiseError to indicate
    a failure to be handled by `.then()`
    """

    pass


class Promise(object):
    """A simple implementation of the Promise specification.
    See: https://promisesaplus.com
    Promise is in essence a syntactic sugar for callbacks. Simplifies passing
    values from functions that might do work in asynchronous manner.
    Example usage:
      * Passing return value of one function to another:
        def do_work_async(resolve):
            # "resolve" is a function that, when called with a value, resolves
            # the promise with provided value and passes the value to the next
            # chained promise.
            resolve(111)  # Can be invoked asynchronously.
        def process_value(value):
            assert value === 111
        Promise(do_work_async).then(process_value)
      * Returning Promise from chained promise:
        def do_work_async_1(resolve):
            # Compute value asynchronously.
            resolve(111)
        def do_work_async_2(resolve):
            # Compute value asynchronously.
            resolve(222)
        def do_more_work_async(value):
            # Do more work with the value asynchronously. For the sake of this
            # example, we don't use 'value' for anything.
            assert value === 111
            return Promise(do_work_async_2)
        def process_value(value):
            assert value === 222
        Promise(do_work_async_1).then(do_more_work_async).then(process_value)
    """

    def __init__(self, executor):
        """Initialize Promise object.
        Arguments:
            executor: A function that is executed immediately by this Promise.
            It gets passed a "resolve" function. The "resolve" function, when
            called, resolves the Promise with the value passed to it.
        """
        self.value = None
        self.resolved = False
        self.mutex = threading.Lock()
        self.callbacks = []
        self._invoke_executor(executor)

    @classmethod
    def resolve(cls, resolve_value=None):
        """Immediatelly resolve a Promise.
        Convenience function for creating a Promise that gets immediately
        resolved with the specified value.
        Arguments:
            resolve_value: The value to resolve the promise with.
        """

        def executor(resolve_fn):
            return resolve_fn(resolve_value)

        return cls(executor)

    def then(self, callback):
        """Create a new promise and chain it with this promise.
        When this promise gets resolved, the callback will be called with the
        value that this promise resolved with.
        Returns a new promise that can be used to do further chaining.
        Arguments:
            callback: The callback to call when this promise gets resolved.
        """

        def callback_wrapper(resolve_fn, resolve_value):
            """A wrapper called when this promise resolves.
            Arguments:
                resolve_fn: A resolve function of newly created promise.
                resolve_value: The value with which this promise resolved.
            """
            result = callback(resolve_value)
            # If returned value is a promise then this promise needs to be
            # resolved with the value of returned promise.
            if isinstance(result, Promise):
                result.then(resolve_fn)
            else:
                resolve_fn(result)

        def sync_executor(resolve_fn):
            """Call resolve_fn immediately with the resolved value.
            An executor that will immediately resolve resolve_fn with the
            resolved value of this promise.
            """
            callback_wrapper(resolve_fn, self._get_value())

        def async_executor(resolve_fn):
            """Queue resolve_fn to be called after this promise resolves later.
            An executor that will resolve received resolve_fn when this promise
            resolves later.
            """
            self._add_callback(functools.partial(callback_wrapper, resolve_fn))

        if self._is_resolved():
            return Promise(sync_executor)
        return Promise(async_executor)

    def _invoke_executor(self, executor):
        def resolve_fn(new_value):
            self._do_resolve(new_value)

        executor(resolve_fn)

    def _do_resolve(self, new_value):
        # No need to block as we can't change from resolved to unresolved.
        if self.resolved:
            raise RuntimeError("cannot set the value of an already resolved promise")
        with self.mutex:
            self.value = new_value
            for callback in self.callbacks:
                callback(new_value)
            self.resolved = True

    def _add_callback(self, callback):
        with self.mutex:
            self.callbacks.append(callback)

    def _is_resolved(self):
        with self.mutex:
            return self.resolved

    def _get_value(self):
        with self.mutex:
            return self.value


class Task(object):
    """
    Task runs a python function `target` when called.
    """

    def __init__(self, target, *args, **kwargs):
        """Initialize the Task object."""
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)


class TaskQueue(Thread):
    """
    A background thread to start all queued processes one after another.
    """

    def __init__(self):
        super().__init__(daemon=True)
        self.queue = Queue()
        self.active_task = None
        self.running = False
        self._block = threading.Lock()

    def __del__(self):
        self.running = False

    def execute(self, task):
        self.queue.put(task)

    def execute_async(self, func, *args, **kwargs):
        return Promise(lambda resolve_fn: self.execute(Task(func, resolve_fn, *args, **kwargs)))

    def cancel_all(self):
        try:
            while not self.Empty():
                self.queue.get_nowait()
                self.queue.task_done()
        except Empty:
            pass

    def busy(self):
        result = False
        with self._block:
            result = self.active_task is not None
        return result

    def run(self):
        self.running = True
        while self.running:
            task = self.queue.get()
            with self._block:
                self.active_task = task
            try:
                task.run()
            except:
                traceback.print_exc()
            finally:
                self.queue.task_done()
                with self._block:
                    self.active_task = None
