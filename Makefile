notebooks := 01-generalites.ipynb \
						 02-langage.ipynb \
						 03-langage.ipynb \
						 04-numpy.ipynb \
						 05-microprojet.ipynb \
						 06-langage.ipynb \
						 07-pandas.ipynb \

local_reveal := False
ifeq ($(local_reveal),True)
# Useful for running in local with internet connexion
  revealprefix := "reveal.js"
else
# Needed for online publication by gitlab pages
  revealprefix := "https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.3.0"
endif

html := $(addprefix build/, $(subst .ipynb,.html,$(notebooks)))
slides := $(addprefix build/, $(subst .ipynb,.slides.html,$(notebooks)))
executed_notebooks := $(addprefix build/, $(notebooks))

.PHONY: all clean html slides executed_notebooks index copy_to_build pdf

all: build html slides index pdf

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  html      to make standalone HTML files"
	@echo "  slides    to make slideshows (use local_reveal=True \
to run them without internet connection)"
	@echo "  pdf       to compile all notebooks as a single PDF book"
	@echo "Use \`make' to run all these targets"

executed_notebooks: copy_to_build $(executed_notebooks)
html: $(html)
slides: copy_reveal $(slides)
index: copy_to_build build/index.html
pdf: copy_to_build build/cours-python.pdf
latex: build/cours-python.tex

define nbconvert
	jupyter nbconvert --to $(1) $< --output-dir=build
endef

build:
	@mkdir -p build

copy_to_build: build
	rsync -ra --delete fig build/
	rsync -ra --delete exos build/

copy_reveal: build
	rsync -ra --delete reveal.js build/

$(executed_notebooks): build/%.ipynb: %.ipynb
	$(call nbconvert,notebook,$<) --execute --allow-errors --ExecutePreprocessor.timeout=60

build/%.html: build/%.ipynb
	$(call nbconvert,html,$<)

build/%.slides.html: build/%.ipynb
	$(call nbconvert,slides,$<) --reveal-prefix $(revealprefix)

build/index.html: index.ipynb
	$(call nbconvert,html,$<)

build/cours-python.tex: executed_notebooks book.tplx
	cd build && python3 -m bookbook.latex --output-file cours-python --template ../book.tplx

build/cours-python.pdf: executed_notebooks book.tplx
	cd build && python3 -m bookbook.latex --pdf --output-file cours-python --template ../book.tplx

clean:
	rm -rf build
