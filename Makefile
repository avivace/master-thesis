betterbib=bibliography_better.bib
TEXFILES := $(shell find . -name '*.tex')
SVGFILES := $(shell find . -name '*.svg')

pdf: revision.tex lint svg
	latexmk --xelatex -latexoption="-shell-escape -8bit" thesis
	make clean

.PHONY : revision.tex
revision.tex:
	printf "%% Autogenerated, do not edit" > revision.tex
	printf '\n\\newcommand{\\revisiondate}{%s}' "$(shell git show -s --format=%ci HEAD)" >> revision.tex
	printf '\n\\newcommand{\\revision}{%s}' "$(shell git log -1 --format=%h)" >> revision.tex

#.PHONY: ${TEXFILES}
#${TEXFILES}: ; latexindent -w -t -s $@

.PHONY: lint
lint: ${TEXFILES}
	-rm chapters/*.bak*
	echo Lint finished

$(betterbib): bibliography.bib
	latexindent -w -t -s bibliography.bib
	betterbib bibliography.bib bibliography_better.bib

.PHONY: ${SVGFILES}
${SVGFILES}: ; inkscape $@ --export-type=pdf

.PHONY: svg
svg: ${SVGFILES}
	echo SVG converted

glossary:
	makeglossaries thesis

publish: pdf
	scp thesis.pdf vps:/var/www/html/thesis.pdf

clean:
	-rm *.acr
	-rm *.alg
	-rm *.glg
	-rm *.gls
	-rm *.xdy
	-rm *.aux
	-rm *.bbl
	-rm *.blg
	-rm *.fdb_latexmk
	-rm *.fls
	-rm *.log
	-rm *.toc
	-rm *.xdv
	-rm *.acn
	-rm *.bbl
	-rm *.blg
	-rm *.ist
	-rm *.log
	-rm *.out
	-rm *.glo
	-rm *.lof
	-rm *.bak*
	-rm *.sbl
	-rm *.slg
	-rm *.sym
	-rm *.bcf
	-rm *.lol
	-rm *.pyg
	-rm *.run.xml
	-rm revision.tex
	-rm bibliography_better.bib