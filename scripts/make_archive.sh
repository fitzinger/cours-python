#!/bin/bash

set -x


# Remove slideshow lines and convert to pdf
cd J1
python ../scripts/process.py --pdf -nb 00-InitPython-generalites.ipynb
python ../scripts/process.py --pdf -nb 01-InitPython-langage.ipynb
cd ../J2
python ../scripts/process.py --pdf -nb 02-InitPython-langage.ipynb
python ../scripts/process.py --pdf -nb 03-InitPython-microprojet.ipynb
cd ../J3
python ../scripts/process.py --pdf -nb 04-InitPython-langage.ipynb
cd ..

incfile="include.lst"

for jour in J1 J2 J3
do
  archive_name="ponte-$jour"

  # Add explicitely named files
  cp ./scripts/manual_include_$jour.lst $incfile
  
  # Add all .py files from exos dirs and image files from fig dirs
  ls $jour/exos/*.py >> $incfile
  ls $jour/fig/* >> $incfile
  
  if [ "$1" == '--zip' ]
  then
    rm -f $archive_name.zip
    zip -r $archive_name.zip -@ < include.lst
  else
    rm -rf $archive_name
    rsync -av --files-from="include.lst" ./  ./$archive_name/
  fi
done
