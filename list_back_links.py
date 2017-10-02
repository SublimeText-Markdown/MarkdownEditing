import sublime, sublime_plugin
import os, string
import re
import mmap

class ListBackLinks(sublime_plugin.TextCommand):
    def run(self, edit):
        print("Listing backlinks")
        self.backlinks = self.find_backlinks()
        self.select_backlink()


    def find_backlinks(self):
        current_file = self.view.file_name()
        current_dir, current_base = os.path.split(current_file)
        current_name, current_extension = os.path.splitext(current_base)

        results = []
        for dirname, _, files in self.list_dir_tree(current_dir):
            for file in files:
                filename = os.path.join(dirname, file)
                if self.contains_wikilink(filename, current_name):
                    results.append(filename)

        return results


    def contains_wikilink(self, filename, current_name):
        link_text = "[[" + current_name + "]]"
        print("Searching %s for: %s" % (filename, current_name))

        try:
            if link_text in open(filename).read():
                return True
        except:
            pass

        return False

    def select_backlink(self):
        self.view.window().show_quick_panel(self.backlinks, self.open_file)


    def open_file(self, selected_index):
        if selected_index != -1:
            file = self.backlinks[selected_index]
            
            print("Opening file '%s'" % (file))
            self.view.window().open_file(file)


    def list_dir_tree(self, directory):
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in dirnames]
            yield dir, dirnames, files

