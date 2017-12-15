notebooks := 01-generalites.ipynb \
						 02-langage.ipynb \
						 03-langage.ipynb \
						 04-numpy.ipynb \
						 05-microprojet.ipynb \
						 06-langage.ipynb \
						 07-pandas.ipynb \

html := $(addprefix build/, $(subst .ipynb,.html,$(notebooks)))
slides := $(addprefix build/, $(subst .ipynb,.slides.html,$(notebooks)))
executed_notebooks := $(addprefix build/, $(notebooks))

.PHONY: all clean html slides executed_notebooks index rsync_to_build copy_to_build pdf

all: build html slides index pdf

html: $(html)
slides: $(slides)
executed_notebooks: $(executed_notebooks)
index: build/index.html
pdf: build/cours-python.pdf
copy_to_build: rsync_to_build build/SIAMGHbook2016.cls

build:
	@mkdir -p build

build/%.html: %.ipynb
	jupyter nbconvert --to html --execute --allow-errors --ExecutePreprocessor.kernel_name=python3 $< --output-dir=build

build/%.slides.html: %.ipynb
	jupyter nbconvert --to slides --execute --allow-errors \
  --reveal-prefix "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.3.0" \
  --ExecutePreprocessor.kernel_name=python3 $< --output-dir=build

$(executed_notebooks): build/%.ipynb: %.ipynb
	jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.kernel_name=python3 $< --output-dir=build

build/index.html: index.ipynb
	jupyter nbconvert --to html --execute --allow-errors --ExecutePreprocessor.kernel_name=python3 $< --output-dir=build

rsync_to_build:
	rsync -ra --delete fig build/
	rsync -ra --delete exos build/

build/SIAMGHbook2016.cls: SIAMGHbook2016.cls
	cp SIAMGHbook2016.cls build

build/cours-python.pdf: build copy_to_build executed_notebooks book.tplx
	cd build && python3 -m bookbook.latex --pdf --output-file cours-python --template ../book.tplx

clean:
	rm -rf build
