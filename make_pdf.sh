#!/bin/bash

set -x

NOTEBOOKS="01-generalites.ipynb
02-langage.ipynb
03-langage.ipynb
04-numpy.ipynb
05-microprojet.ipynb
06-langage.ipynb
07-pandas.ipynb
"

rm -rf build
mkdir -p build

for notebook in $NOTEBOOKS
do
  jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.kernel_name=python3 $notebook --output=build/$notebook
done

cp book.tplx build
cp SIAMGHbook2016.cls build
cd build

python3 -m bookbook.latex --pdf --output-file python --template book.tplx
