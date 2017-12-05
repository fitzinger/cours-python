#!/bin/bash

if [ $# -eq 0 ]; then
  echo Usage: `basename $0` 1, 2, 3 or 4 [--execute] 1>&2
  exit 1
fi

port=`expr 8000 + $1`

case $1 in
  "1")
      nbdir="01-CoursPython-generalites"
      ;;
  "2")
      nbdir="02-CoursPython-langage"
      ;;
  "3")
      nbdir="03-CoursPython-langage"
      ;;
  "4")
      nbdir="04-CoursPython-numpy"
      ;;
  "5")
      nbdir="05-CoursPython-microprojet"
      ;;
  "6")
      nbdir="06-CoursPython-langage"
      ;;
  *)
      exit
      ;;
  esac
  nbfile=$nbdir.ipynb
set -x
cd $nbdir
jupyter-nbconvert $nbfile --to slides --post serve $2 --allow-errors --ServePostProcessor.port=$port
