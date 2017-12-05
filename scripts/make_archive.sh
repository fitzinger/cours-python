#!/bin/bash

set -x

incfile="include.lst"

# Remove slideshow lines and convert to pdf
notebooks="01-CoursPython-generalites \
           02-CoursPython-langage \
           03-CoursPython-langage \
           04-CoursPython-numpy \
           05-CoursPython-microprojet"

for notebook in $notebooks
do
  cd $notebook
  ../scripts/process.py --pdf -nb $notebook.ipynb
 
  archive_name="ponte-$notebook"

  # Add explicitely named files
  cp ../scripts/manual_include_$notebook.lst $incfile
  
  # Add all .py files from exos dirs and image files from fig dirs
  echo "$notebook.ipynb" >> $incfile
  echo "$notebook.pdf" >> $incfile
  ls exos/*.py 2>/dev/null >> $incfile  
  ls fig/* >> $incfile
  
  if [ "$1" == '--zip' ]
  then
    rm -f $archive_name.zip
    zip -r $archive_name.zip -@ < include.lst
    cp $archive_name.zip ../public/
  else
    rm -rf ../public/$archive_name
    rsync -av --files-from="include.lst" ./  ../public/$archive_name/
  fi
  cd ..
done
