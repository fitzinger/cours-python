#!/bin/bash

if [ $# -eq 0 ]; then
  echo Usage: `basename $0` 0, 1, 2, 3 or 4 [--execute] 1>&2
  exit 1
fi

port=`expr 8000 + $1`

case $1 in
  "0")
      nbdir=J1
      nbfile="00-InitPython-generalites.ipynb"
      ;;
  "1")
      nbdir=J1
      nbfile="01-InitPython-langage.ipynb"
      ;;
  "2")
      nbdir=J2
      nbfile="02-InitPython-langage.ipynb"
      ;;
  "3")
      nbdir=J2
      nbfile="03-InitPython-microprojet.ipynb"
      ;;
  "4")
      nbdir=J3
      nbfile="04-InitPython-langage.ipynb"
      ;;
  *)
      exit
      ;;
  esac
set -x
cd $nbdir
jupyter-nbconvert $nbfile --to slides --post serve $2 --allow-errors --ServePostProcessor.port=$port
