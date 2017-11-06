#/bin/bash

set -x

if [ "$1" != "--url" ]
then
  # Useful for running in local with internet connexion
  revealprefix="reveal.js"
else
  # Needed for online publication by gitlab pages
  revealprefix="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.3.0"
fi

notebooks="J1/00-InitPython-generalites.ipynb \
           J1/01-InitPython-langage.ipynb \
           J2/02-InitPython-langage.ipynb \
           J2/03-InitPython-microprojet.ipynb \
           J3/04-InitPython-langage.ipynb" 

jupyter-nbconvert $notebooks --to slides --reveal-prefix $revealprefix --output-dir=public

jupyter-nbconvert index.ipynb --to html --output-dir=public

cp J*/*-InitPython-*.ipynb public  # uploaded notebooks will be rendered by nbviewer

if [ "$1" != "--url" ]
then
  cp -r reveal.js public/
fi

cp -r J1/fig public
cp J2/fig/* public/fig


