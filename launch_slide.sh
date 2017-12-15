#!/bin/bash

if [ $# -eq 0 ]; then
  echo Usage: `basename $0` notebook.ipynb [--execute] 1>&2
  exit 1
fi

notebook=$(basename "$1" .ipynb)
port_index="${notebook:0:2}"
port=`expr 8000 + $port_index`

set -x
jupyter-nbconvert $notebook.ipynb --to slides --post serve $2 --allow-errors --ServePostProcessor.port=$port
