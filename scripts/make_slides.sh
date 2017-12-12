#/bin/bash

set -x

if [ "$1" != "--url" ]
then
  # Useful for running in local with internet connexion
  revealprefix="reveal.js"
  cp -r reveal.js public/
else
  # Needed for online publication by gitlab pages
  revealprefix="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.3.0"
fi

notebooks="01-CoursPython-generalites/01-CoursPython-generalites.ipynb \
           02-CoursPython-langage/02-CoursPython-langage.ipynb \
           03-CoursPython-langage/03-CoursPython-langage.ipynb \
           04-CoursPython-numpy/04-CoursPython-numpy.ipynb \
           05-CoursPython-microprojet/05-CoursPython-microprojet.ipynb \
           06-CoursPython-langage/06-CoursPython-langage.ipynb \
           07-CoursPython-pandas/07-CoursPython-pandas.ipynb"

jupyter-nbconvert $notebooks --to slides --reveal-prefix $revealprefix --output-dir=public

jupyter-nbconvert index.ipynb --to html --output-dir=public

cp *-CoursPython-*/*-CoursPython-*.ipynb public  # uploaded notebooks will be rendered by nbviewer

mkdir public/fig
cp 01-CoursPython-generalites/fig/* public/fig
cp 02-CoursPython-langage/fig/* public/fig
cp 03-CoursPython-langage/fig/* public/fig
cp 04-CoursPython-numpy/fig/* public/fig
cp 05-CoursPython-microprojet/fig/* public/fig
cp 06-CoursPython-langage/fig/* public/fig
cp 07-CoursPython-pandas/fig/* public/fig


