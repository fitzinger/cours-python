#!/usr/bin/env python3
"""
Generate index.html
"""
import os
import jinja2
import yaml
from pprint import pprint
from markdown import markdown


SCRIPT_PATH = os.path.relpath(os.path.join(os.path.dirname(__file__)))
VARIABLES_FILE = os.path.join(SCRIPT_PATH, "variables.yml")
HTML_TEMPLATE = "homepage.html"
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


def render(html_filename, html_template, variables):

    # Inject html table, title and comment into html_template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(SCRIPT_PATH))
    template = env.get_template(html_template)
    html_out = template.render(variables)
    with open(html_filename, 'w') as f:
        f.write(html_out)

def markdown2html(markdown_file):
    with open(os.path.join(SCRIPT_PATH, markdown_file), 'r') as f:
        md = f.read()
    return markdown(md, extensions=['fenced_code', 'codehilite'])

def main():
    # Render homepage
    homepage_variables = get_variables()
    print(">>> Homepage template variables:")
    pprint(homepage_variables)
    render('index.html', HTML_TEMPLATE, homepage_variables)

    # Render doc
    content = {'article_content': markdown2html("install_anaconda.md")}
    render('install_anaconda.html', 'article.html', content)

if __name__ == '__main__':
    main()
