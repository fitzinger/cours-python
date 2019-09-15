#!/usr/bin/env python3
"""
Generate index.html
"""
import os
import jinja2
import yaml
from pprint import pprint


script_path = os.path.relpath(os.path.join(os.path.dirname(__file__)))
VARIABLES_FILE = os.path.join(script_path, "variables.yml")
HTML_TEMPLATE = "template.html"
print(HTML_TEMPLATE)
ENV_VARIABLE_PREFIX = 'COURSE'


def get_variables(variables_file=VARIABLES_FILE):
    """Parse yaml file and return the corresponding configuration dictionary"""
    with open(variables_file, 'r') as f:
        variables = yaml.safe_load(f)
    # Update config with environment variable (type COURSE_GITLAB_URL)
    # if exists
    for variable in variables:
        environment_variable = '{}_{}'.format(ENV_VARIABLE_PREFIX,
                                              variable.upper())
        variables[variable] = os.environ.get(environment_variable,
                                             variables[variable])
    # Make ichapter > working_chapter unavailable for download
    working_chapter = os.environ.get('{}_WORKING_CHAPTER'.format(
                                     ENV_VARIABLE_PREFIX))
    if working_chapter:
        working_chapter = int(working_chapter)
        for ichapter, chapter in enumerate(variables['chapters']):
            print(ichapter, chapter)
            if ichapter >= working_chapter:
                variables['chapters'][ichapter]['preview_only'] = True

    return variables


def main():
    variables = get_variables()
    print(">>> Template variables:")
    pprint(variables)

    # Inject html table, title and comment into html_template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(script_path))
    template = env.get_template(HTML_TEMPLATE)
    html_out = template.render(variables)
    with open('index.html', 'w') as f:
        f.write(html_out)


if __name__ == '__main__':
    main()
