import os
import filemanager

#Soll GrADS Aufrufe auf plot.gs und line.gs verpacken.

#Ruft GrADS mit Parameter CMD auf
def call(script, outputdir, name, lat, lon, gmt, dirname, title, tend, unit, params):
	fullcall = str(script) + " " + str(outputdir) + " " + name + " " + str(lat) + " " + str(lon) + " " + str(gmt) + " " + dirname + " " + title + " " + tend + " " + unit + " " + params + " 0"
	oscall(fullcall)

def area(script, outdir, name, lat, lon, area, gmt, title, frontpara, backpara, color):
	fullcall = str(script) + " " + str(outdir) + " " + str(name) + " " + str(lat) + " " + str(lon) + " " + str(area) + " " + str(gmt) + " " + str(title) + " " + str(frontpara) + " " + str(backpara) + " " + str(color)
	oscall(fullcall)

def oscall(gradspara):
	gradscall = "grads -b -a "+str(4./3)+" -x -c \"run "+ gradspara + "\""
	#print gradscall  + " >/dev/null 2>/dev/null"
	os.system(gradscall + " >/dev/null 2>/dev/null")

def main():
	print "run AuVi.py for standart routine"

if __name__ == "__main__":
	main()