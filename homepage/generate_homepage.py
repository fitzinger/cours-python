#!/usr/bin/env python3
"""
Generate index.html
"""
import os
import jinja2
import yaml

script_path = os.path.relpath(os.path.join(os.path.dirname(__file__)))
CONFIG_FILE = os.path.join(script_path, "config.yml")
HTML_TEMPLATE = "template.html"
print(HTML_TEMPLATE)

def get_config(config_file=CONFIG_FILE):
    """Parse yaml file and return the corresponding configuration dictionary"""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def main():
    config = get_config()

    # Inject html table, title and comment into html_template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(script_path))
    template = env.get_template(HTML_TEMPLATE)
    html_out = template.render(config)
    with open('index.html', 'w') as f:
        f.write(html_out)


if __name__ == '__main__':
    main()
