bll: bll.tex
	rm bll.pdf                     || echo ""
	xelatex bll.tex >/dev/null     || echo ""
	bibtex bll      >/dev/null     || echo ""
	xelatex bll.tex >/dev/null     || echo ""
	rm *.aux *.toc *.log *.blg *.xml *.bbl bll-blx.bib
