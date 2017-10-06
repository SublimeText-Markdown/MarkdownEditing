import sublime, sublime_plugin
import os, string

try:
    from MarkdownWiki.open_page import *
except ImportError:
    from open_page import *


MARKDOWN_EXTENSION = '.md'
PAGE_REF_FORMAT = '[[%s]]'


class ListBackLinks(OpenPage):
    def run(self, edit):
        print("Listing file_list")
        self.file_list = self.find_files_with_ref()
        self.select_backlink()


    def find_files_with_ref(self):
        self.current_file = self.view.file_name()
        self.current_dir, current_base = os.path.split(self.current_file)
        self.current_name, current_extension = os.path.splitext(current_base)

        results = []
        for dirname, _, files in self.list_dir_tree(self.current_dir):
            for file in files:
                page_name, extension = os.path.splitext(file)
                filename = os.path.join(dirname, file)
                if extension == MARKDOWN_EXTENSION and self.contains_ref(filename, self.current_name):
                    results.append([page_name, filename])

        return results


    def contains_ref(self, filename, page_name):
        link_text = PAGE_REF_FORMAT % page_name

        try:
            if link_text in open(filename).read():
                return True
        except:
            pass

        return False

    def select_backlink(self):
        self.view.window().show_quick_panel(self.file_list, self.open_selected_file)

