import sublime, sublime_plugin
import os, string
import re

class OpenPage(sublime_plugin.TextCommand):
    def run(self, edit):
        page = self.identify_page()

        print("Open page: %s" % (page))
        self.select_page(page)


    def identify_page(self):
        for region in self.view.sel():
            text_on_cursor = None
            if region.begin() == region.end():
                word = self.view.word(region)
                if not word.empty():
                    text_on_cursor = self.view.substr(word)
                    return text_on_cursor

        return None


    def select_page(self, pagename):
        if pagename:
            self.potential_files = self.find_files(pagename)

        if len(self.potential_files) > 1:
            self.view.window().show_quick_panel(self.potential_files, self.open_file)
        elif len(self.potential_files) == 1:
            self.open_file(0)
        else:
            self.new_file(pagename)


    def find_files(self, pagename):
        pagename = pagename.replace('\\', os.sep).replace(os.sep+os.sep, os.sep).strip()

        current_file = self.view.file_name()
        _, current_extension = os.path.splitext(current_file)
        current_dir = os.path.dirname(current_file)

        pagename = pagename + current_extension
        print("Locating page '%s' in: %s" % (pagename, current_dir) )

        results = []
        for dirname, _, files in self.list_dir_tree(current_dir):
            for file in files:
                fileName = os.path.join(dirname, file)
                if re.search(pagename, fileName):
                    results.append(fileName)

        return results


    def new_file(self, pagename):
        current_file = self.view.file_name()
        _, current_extension = os.path.splitext(current_file)
        current_dir = os.path.dirname(current_file)

        filename = os.path.join(current_dir, pagename + current_extension)

        new_view = self.view.window().new_file()
        new_view.retarget(filename)
        new_view.run_command('save')


    def open_file(self, selected_index):
        if selected_index != -1:
            file = self.potential_files[selected_index]
            
            print("Opening file '%s'" % (file))
            self.view.window().open_file(file)


    def list_dir_tree(self, directory):
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in dirnames]
            yield dir, dirnames, files

