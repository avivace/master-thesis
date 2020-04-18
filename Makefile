betterbib:
	betterbib bibliography.bib bibliography_better.bib

pdf: betterbib
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