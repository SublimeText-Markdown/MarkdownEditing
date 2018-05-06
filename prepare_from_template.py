import sublime, sublime_plugin

import sys
import os.path

from string import Template


DEFAULT_PAGE_TEMPLATE = "templates/PageTemplate.md"
PRESET_TEMPLATE_TEXT = "# $title\n\n"

class PrepareFromTemplateCommand(sublime_plugin.TextCommand):
    def run(self, edit, **args):
        """Prepare a new page content from a named template triggered from run command 'prepare_from_template'.

        :Example:

        view.run_command('prepare_from_template', {
            'title': pagename,
            'template': 'default_page'
        })

        :param self: This command instance
        :param edit: The sublime edit instance
        :param args: The command arguments including 'title' and 'template'
        """

        print("Running PrepareFromTemplateCommand")
        template_name = args['template']
        print("Creating new page from template: ", template_name)

        text = self.generate_from_template(template_name, args)
        self.view.insert(edit, 0, text)

    def generate_from_template(self, template_name, args):
        """Generate the text using the template"""

        template_text = self.retrieve_template_text(template_name)
        template = Template(template_text)
        return template.substitute(args)

    def retrieve_template_text(self, template_name):
        """Retrieve the template text.

        The setting 'mde.wikilinks.templates' may be configured with a filename for 
        the template.  This file (if it exists) will be loaded otherwise the preset 
        template will be used
        """

        template = self.view.settings().get("mde.wikilinks.templates", DEFAULT_PAGE_TEMPLATE)
    
        if not os.path.isfile(template):
            current_file = self.view.file_name()
            current_dir = os.path.dirname(current_file)
            template = os.path.join(current_dir, template)

        if os.path.isfile(template):
            print("Using template:", template)
            try:
                with open(template, 'rt') as f:
                    return f.read()
            except:
                print("Unable to read template:", sys.exc_info()[0])

        # Unable to load template  so using preset template 
        print("Template:", template, "not found.  Using preset.")
        return PRESET_TEMPLATE_TEXT
