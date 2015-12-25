bll: bll.tex
	rm bll.pdf                     || echo ""
	xelatex bll.tex >/dev/null     || echo ""
	bibtex bll      >/dev/null     || echo ""
	xelatex bll.tex >/dev/null     || echo ""
	rm *.aux *.toc *.log *.blg *.xml *.bbl bll-blx.bib
out: bll.tex
	rm bll.pdf || echo "Nothing to delete!"
	xelatex bll.tex
	bibtex bll
	xelatex bll.tex
	rm *.aux *.toc *.log *.blg *.xml *.bbl bll-blx.bib
new:
	xelatex --interaction=nonstopmode bll.tex || echo "first run"
	bibtex bll
	xelatex --interaction=nonstopmode bll.tex
	exit 0
clean:
	rm *.aux *.toc *.log *.blg *.xml *.bbl bll-blx.bib || echo "deleted"
	rm bll.pdf || echo "deleted"
