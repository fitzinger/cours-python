#!/usr/bin/env python3
"""
Generate index.html
"""
import jinja2
import yaml
 

CONFIG_FILE = "config.yml"
HTML_TEMPLATE = "template.html"


def get_config(config_file=CONFIG_FILE):
    """Parse yaml file and return the corresponding configuration dictionary"""
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def main():
    config = get_config()
    # df = pd.read_csv(config['csv_file'])

    # # Format Firstname and Lastname
    # for field in 'First name', 'Last name':
    #     df[field] = df[field].apply(lambda s: s.strip().title())

    # # Nom = Firstname Lastname
    # df['Nom'] = df['First name'] + ' ' + df['Last name']

    # # Create a dataframe for html export
    # df_out = df[['Nom', 'Institution']].copy()
    # df_out["Signature"] = ""
    # df_out["OK"] = ""

    # # Create html table
    # table = df_out.to_html(index=False)

    # Inject html table, title and comment into html_template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('.'))
    template = env.get_template(HTML_TEMPLATE)
    template_vars = {'title': config['title'],
                     'subtitle': config['subtitle'],
                     'authors': config['authors']
                    }
    html_out = template.render(template_vars)
    with open('index.html', 'w') as f:
        f.write(html_out)


if __name__ == '__main__':
    main()