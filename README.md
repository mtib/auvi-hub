# AuVi - Hub
[![Build Status](https://travis-ci.org/tibyte/auvi-hub.svg?branch=master)](https://travis-ci.org/tibyte/auvi-hub)

This is the EAA (Extra Academic Activity) by Markus Becker

You can have a look at the built documentation [here](http://viwetter.de/ci/Latex/Lernleistung/bll.pdf).

My Project Manager is Dr. Ronald Eixmann
I need to mention my ex-co-worker Swenja Wagner as a big influence on this project.

## File Structure
This Project is structured in Code (mostly python2.7) and LaTeX.

## Running our Program
If you want to truly understand what is happening and you speak german, you should be able to read our documentation, otherwise, as long as we haven't written a english version of that, you probably have to reverse engineer our code.

The start point for our program is [auvi.py](/Code/PyVi/auvi.py).

## Compiling documentation
```bash
cd Latex/Lernleistung
xelatex bll.tex
bibtex bll
xelatex bll.tex
```
This needs texlive or mktex to be installed as well as xetex or xelatex and bib(la)tex. You might be able to run another version of Latex, but I am only testing it to be compatible with xelatex.

## Contact
If you want to contact me directly about this project, do so via GitHub. Otherwise please email me: [Markus Becker](mailto:markus@tibyte.net?subject=AuVi)
