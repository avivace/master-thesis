betterbib=bibliography_better.bib
TEXFILES := $(shell find . -name '*.tex')

.PHONY: ${TEXFILES}
${TEXFILES}: ; latexindent -w -t -s $@

.PHONY: lint
lint: ${TEXFILES}
	rm *.bak*
	echo Lint finished

$(betterbib): bibliography.bib
	latexindent -w -t -s bibliography.bib
	betterbib bibliography.bib bibliography_better.bib

pdf: $(betterbib) lint
	latexmk --xelatex thesis

publish: pdf
	scp thesis.pdf vps:/var/www/html/thesis.pdf

clean:
	rm *.aux
	rm *.bbl
	rm *.blg
	rm *.fdb_latexmk
	rm *.fls
	rm *.log
	rm *.toc
	rm *.xdv
	rm bibliography_better.bib