import logging
import sublime

PACKAGE_NAME = __package__.split(".", 1)[0]

logging.basicConfig(level=logging.ERROR, format="%(name)s [%(levelname)s]: %(message)s")
logger = logging.getLogger(PACKAGE_NAME)


def load_logger():
    """
    Subscribe to Preferences changes in to get log level from user settings.

    Must be called in plugin_loaded().
    """
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.clear_on_change(__name__)
    settings.add_on_change(__name__, on_preferences_changed)
    on_preferences_changed()


def unload_logger():
    """
    Unsubscribe to Preferences changes.

    Must be called in plugin_unloaded().
    """
    settings = sublime.load_settings("Preferences.sublime-settings")
    settings.clear_on_change(__name__)


def on_preferences_changed():
    """
    Update log level according to user settings
    """
    settings = sublime.load_settings("Preferences.sublime-settings")

    try:
        logger.setLevel(settings.get("mde.logging.level", "ERROR"))
    except (TypeError, ValueError):
        logger.setLevel(logging.ERROR)
