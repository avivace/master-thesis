pdf:
	latexmk --xelatex thesis

publish: pdf
	scp thesis.pdf vps:/var/www/html/thesis.pdf