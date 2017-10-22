import sublime, sublime_plugin
import os, string

MARKDOWN_EXTENSION = '.md'

class MakePageReferenceCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.word_region = self.select_word_at_cursor()
        self.file_list = self.find_matching_files()

        if self.word_region:
            self.make_page_reference(edit)

        if len(self.file_list) > 1:
            self.view.window().show_quick_panel(self.file_list, self.use_selected_file)

    def use_selected_file(self, selected_index):
        if selected_index != -1:
            page_name, file = self.file_list[selected_index]
            
            print("Using selected page '%s'" % (page_name))
            self.view.run_command('replace_selected', {'text': page_name})

    def select_word_at_cursor(self):
        selection = self.view.sel()
        for region in selection:
            word_region = self.view.word(region)
            if not word_region.empty():
                selection.clear()
                selection.add(word_region)
                return word_region

        return None

    def find_matching_files(self):
        word = self.view.substr(self.word_region)
        print("Searching for '%s'" % (word))

        self.current_file = self.view.file_name()
        self.current_dir, current_base = os.path.split(self.current_file)
        self.current_name, current_extension = os.path.splitext(current_base)

        results = []
        for dirname, _, files in self.list_dir_tree(self.current_dir):
            for file in files:
                page_name, extension = os.path.splitext(file)
                filename = os.path.join(dirname, file)

                if extension == MARKDOWN_EXTENSION and word in page_name:
                    results.append([page_name, filename])

        return results

    def list_dir_tree(self, directory):
        for dir, dirnames, files in os.walk(directory):
            dirnames[:] = [dirname for dirname in dirnames]
            yield dir, dirnames, files

    def make_page_reference(self, edit):
        self.view.insert(edit, self.word_region.end(), "]]")
        self.view.insert(edit, self.word_region.begin(), "[[")
