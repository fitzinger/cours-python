#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Process notebooks"""

import argparse
from latex import build_pdf, LatexBuildError
import os
import shlex
import subprocess as sp


def run_cmd(cmd):
    """Execute command system cmd"""

    print(">>> Executing: ", cmd)

    args = shlex.split(cmd)  # Split cmd into arguments
    return sp.call(args)


def remove_line(file_name, bad_strings):
    """remove bad strings line from_filename"""

    print(">>> From {}, removing lines containing: ".format(file_name))
    for line in bad_strings:
        print("\t", line)

    with open(file_name, 'r') as in_file:
        data = in_file.readlines()
        newdata = [line for line in data
                   if not any(bad_string in line
                              for bad_string in bad_strings)]

    with open(file_name, 'w') as out_file:
        out_file.writelines(newdata)


def add_line(file_name, in_line, line_to_add, place='after'):
    """Add a line after a given line in file_name"""

    with open(file_name, 'r') as in_file:
        data = in_file.readlines()
        newdata = []
        for line in data:
            if in_line in line:
                if place == 'after':
                    newdata.append(line)
                    newdata.append(line_to_add)
                else:
                    newdata.append(line_to_add)
                    newdata.append(line)
            else:
                newdata.append(line)

    with open(file_name, 'w') as out_file:
        out_file.writelines(newdata)


def replace_string(file_name, old_string, new_string):
    """Replace old_string by new_string in file_name"""

    with open(file_name, 'r') as in_file:
        data = in_file.read()
        newdata = data.replace(old_string, new_string)

    with open(file_name, 'w') as out_file:
        out_file.write(newdata)


def remove_from_latex(tex_file_name, block_start, block_end):
    """Remove block of lines that cannot be compiled with pdflatex"""

    with open(tex_file_name, 'r') as in_file:
        content = in_file.readlines()
        # Get index of line containing block_start
        istart = 0
        iend = 0
        for (index, line) in enumerate(content):
            if block_start in line:
                istart = index
            elif block_end in line:
                iend = index
                break

        if istart and iend:
            removed = content[istart:iend]
            print(">>> Warning! The following lines will be removed",
                  "from {}:\n".format(tex_file_name))
            for line in removed:
                print("\t", line)
            print("because they cannot be compiled with pdflatex.")
            newcontent = content[:istart] + content[iend:]
        else:
            newcontent = content

    with open(tex_file_name, 'w') as out_file:
        out_file.writelines(newcontent)


def clean_latex_files(notebook_file_name):
    """Clean .tex, .log, .aux, out, pdf files corresponding to notebook"""

    extensions = (".tex", ".log", ".aux", ".out", ".synctex.gz", ".pdf")
    prefix = notebook_file_name.split('.ipynb')[0]
    print(">>> Cleaning files")
    for extension in extensions:
        file_name = prefix + extension
        try:
            os.remove(file_name)
            print("\t", file_name)
        except OSError:
            pass


def latex_to_pdf(tex_file_name):
    """Convert .tex file to pdf using tex module """

    pdf_file_name = tex_file_name.replace('.tex', '.pdf')
    print(">>> Converting {} to {}".format(tex_file_name, pdf_file_name))

    # Remove carriage return character
    block_start = "\subsubsection*{Mode Edition}\label{mode-edition}"
    block_end = "\subsubsection*{Note :}\label{note}"
    remove_from_latex(tex_file_name, block_start, block_end)

    # Remove block containing chess and Japanese characters
    block_start = "Exemples de caractères spéciaux :"
    block_end = "Pour une liste de caractères unicode"
    remove_from_latex(tex_file_name, block_start, block_end)

    # Require to work in current working dir because figure path are relative
    current_dir = os.getcwd()
    try:
        pdf = build_pdf(open(tex_file_name), texinputs=[current_dir, ''])
        pdf.save_to(pdf_file_name)
    except LatexBuildError as e:
        for err in e.get_errors():
            print('Error in {0[filename]}, line {0[line]}: {0[error]}'
                  .format(err))
            for msg in err['context'][1:]:
                print('    {}'.format(msg.decode('utf-8')))
            print()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Process notebook files")
    parser.add_argument('-nb', '--notebook',
                        help="Notebook file name (all notebooks if blank)")
    parser.add_argument('--pdf', action='store_true',
                        help="Convert to pdf using latex")

    args = parser.parse_args()
    if args.notebook:  # notebook file name is given as argument
        notebooks = (args.notebook,)
    else:
        notebooks = ('01-CoursPython-generalites.ipynb',
                     '02-CoursPython-langage.ipynb')

    for notebook in notebooks:

        print(">> Processing:", notebook)

        # Remove slideshow display in notebook
        bad_strings = ['  "celltoolbar": "Slideshow",\n']
        remove_line(notebook, bad_strings)

        if args.pdf:
            print(">>> Converting to pdf")
            # Clean files
            clean_latex_files(notebook)

            # Run notebook conversion to LaTeX
            cmd = "jupyter-nbconvert {} --to latex --execute --allow-errors"\
                  .format(notebook)
            p = run_cmd(cmd)

            # Remove unwanted lines in .tex file
            bad_strings = ['\caption{}', '\maketitle']
            latexfile = notebook.replace('.ipynb', '.tex')
            remove_line(latexfile, bad_strings)

            # Add usepacakage to .tex file header
            in_line = "\\usepackage{graphicx}"
            line_to_add = "    \\usepackage{textcomp}\n" \
                          "    \\usepackage{caption}\n"

            add_line(latexfile, in_line, line_to_add)

            # Insert new page before new section
            in_line = "    \section"
            line_to_add = "\\newpage\n"
            add_line(latexfile, in_line, line_to_add, place='before')

            # Replace some strings to scale figures
            # and perform some corrections
            old2new = {
                       #"{fig/compile_interprete.png}":
                       #"[width=17cm]{fig/compile_interprete.png}",
                       #"{fig/spyder.png}":
                       #"[width=17cm]{fig/spyder.png}",
                       #"{fig/meld.png}":
                       #"[width=17cm]{fig/meld.png}",
                       "\includegraphics{https://upload.wikimedia.org/"
                       "wikipedia/commons/thumb/6/60/Tower_of_Hanoi_4.gif/"
                       "260px-Tower_of_Hanoi_4.gif}":
                       "\captionsetup{labelformat=empty}\n"
                       "\includegraphics{fig/Tower_of_Hanoi.jpeg}\n"
                       "\caption{\href{https://upload.wikimedia.org/"
                       "wikipedia/commons/thumb/6/60/Tower_of_Hanoi_4.gif/"
                       "260px-Tower_of_Hanoi_4.gif}"
                       "{Cliquer ici pour la version animée}}\n",
                       "section{": "section*{"
                       }

            for old, new in old2new.items():
                replace_string(latexfile, old, new)

            latex_to_pdf(latexfile)
