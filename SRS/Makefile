MAIN = main


help:
	# t --- tex
	# s --- show
	# c --- clean

t:
	latexmk -xelatex -shell-escape $(MAIN)

s:
	qpdfview $(MAIN).pdf

c:
	latexmk -c
