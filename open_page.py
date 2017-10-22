import sublime, sublime_plugin
import os, string
import re

class OpenPageCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        pagename = self.identify_page_at_cursor()
        self.select_page(pagename)


    def identify_page_at_cursor(self):
        for region in self.view.sel():
            text_on_cursor = None

            pos = region.begin()
            scope_region = self.view.extract_scope(pos)
            if not scope_region.empty():
                text_on_cursor = self.view.substr(scope_region)
                return text_on_cursor.strip(string.punctuation)

        return None


    def select_page(self, pagename):
        print("Open page: %s" % (pagename))

        if pagename:
            self.file_list = self.find_files_with_name(pagename)

        if len(self.file_list) > 1:
            self.view.window().show_quick_panel(self.file_list, self.open_selected_file)
        elif len(self.file_list) == 1:
            self.open_selected_file(0)
        else:
            self.open_new_file(pagename)


    def find_files_with_name(self, pagename):
        pagename = pagename.replace('\\', os.sep).replace(os.sep+os.sep, os.sep).strip()

        self.current_file = self.view.file_name()
        _, current_extension = os.path.splitext(self.current_file)
        self.current_dir = os.path.dirname(self.current_file)

        print("Locating page '%s' in: %s" % (pagename, self.current_dir) )

        search_pattern = "^%s%s$" % (pagename, current_extension)
        results = []
        for dirname, _, files in self.list_dir_tree(self.current_dir):
            for file in files:
                if re.search(search_pattern, file):
                    filename = os.path.join(dirname, file)
                    results.append([self.extract_page_name(filename), filename])

        return results


    def open_new_file(self, pagename):
        current_syntax = self.view.settings().get('syntax')
        current_file = self.view.file_name()
        _, current_extension = os.path.splitext(current_file)
        current_dir = os.path.dirname(current_file)

        filename = os.path.join(current_dir, pagename + current_extension)

        new_view = self.view.window().new_file()
        new_view.retarget(filename)
        new_view.run_command('prepare_from_template', {
            'title': pagename,
            'template': 'default_page'
        })
        print("Current syntax: %s" % current_syntax)
        new_view.set_syntax_file(current_syntax)

        # Create but don't save page
        # new_view.run_command('save')


    def open_selected_file(self, selected_index):
        if selected_index != -1:
            _, file = self.file_list[selected_index]
            
            print("Opening file '%s'" % (file))
            self.view.window().open_file(file)

    def extract_page_name(self, filename):
        _, base_name = os.path.split(filename)
        page_name, _ = os.path.splitext(base_name)

        return page_name;


    def list_dir_tree(self, directory):
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in dirnames]
            yield dir, dirnames, files

