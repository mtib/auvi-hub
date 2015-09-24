import filemanager
import grads
import sys

VERSION = "1.0"
auvidir = ""

def main(args):
	greet()
	run()

def run():
	filemanager.createOutputDirs()
	auvidir = filemanager.getAuViDir()
	outdir = auvidir+"output/"
	gradsdir = auvidir+"grads/"
	gradsline = gradsdir+"line.gs"
	gradsplot = gradsdir+"plot.gs"
	loc = filemanager.getLoc()
	locpara = filemanager.getLocPara()
	arepara = filemanager.getArePara()
	for location in loc:
		name = location[0]
		lat = location[1]
		lon = location[2]
		gmt = location[4]
		for attr in locpara:
			dirname = attr[1]
			title = attr[0]
			tend = "grads"
			unit = attr[3]
			params = attr[2]
			print name + " " + dirname + " " + tend
			grads.call(gradsline,outdir,name,lat,lon,gmt,dirname,title,tend,unit,params)
	for para in arepara:
		for location in loc:
			print location[0] + " " + para[1]
			grads.area(gradsplot, outdir, location[0], location[1], location[2], location[3], location[4], para[0], para[1], para[2], auvidir+"grads/"+para[4])
	filemanager.convertToGifs()
	filemanager.moveOutputToWeb()

def greet():
	print "This is Python-AuVi Version: " + str(VERSION)


if __name__ == "__main__":
	main(sys.argv[1:])
