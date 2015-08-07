import json

#Constants
LOCALS_FILE = "locals.json"
LOCALS_PARAM_FILE = "locals_param.json"
AREA_FILE = "areas.json"
AREA_PARAM_FILE = "areas_param.json"
EMPTY_ERROR = "Nothing to list"
DEFAULT_FRONT = "Front" #Ordner
DEFAULT_BACK = "Back" #GrADS
#Add new Locale
def writeNewLocale(ort,lat,lon,area,gmtdif):
	appendToJsonFile(LOCALS_FILE,[ort,lat,lon,area,gmtdif])
	print LOCALS_FILE + " <= " + str([ort,lat,lon,area,gmtdif])

#Add line parameter, front and back are strings. front for folders, back for GrADS
def writeNewLParam(name, front, back, unit):
	appendToJsonFile(LOCALS_PARAM_FILE,[name, front, back, unit])
	print LOCALS_PARAM_FILE + " <= " + str([name, front, back, unit])

#Add plot parameter, front and back are strings. front for folders, back for GrADS
def writeNewAParam(name, front, back, unit, colorsheme):
	appendToJsonFile(AREA_PARAM_FILE,[name, front, back, unit, colorsheme])
	print AREA_PARAM_FILE + " <= " + str([name, front, back, unit, colorsheme])

def writeNewArea(ort,lat,lon,area,gmtdif=1):
	appendToJsonFile(AREA_FILE,[ort,lat,lon,area,gmtdif])
	print AREA_FILE + " <= " + str([ort,lat,lon,area,gmtdif])

#Appends the appendix to the file_name provided
def appendToJsonFile(file_name, appendix):
	f = open(file_name,"r")
	a = []
	if len(f.read()) != 0:
		f.seek(0)
		a = json.load(f)
	a.append(appendix)
	f.close()
	f = open(file_name,"w")
	json.dump(a,f)
	f.close


def listLocales():
	listPoints(LOCALS_FILE)

def listAreas():
	listPoints(AREA_FILE)

def listPoints(file_name):
	f = open(file_name,"r")
	a=[]
	if len(f.read()) != 0:
		f.seek(0)
		a = json.load(f)
		f.close()
	else:
		print EMPTY_ERROR
		f.close()
		return
	a.insert(0,["Ort", "Lat", "Lon", "Area", "GMT"])
	m = []
	for i in range(len(a[0])):
		m.append(len(str(a[0][i])))
	for l in a:
		c = 0
		for i in l:
			if len(str(i))>m[c]:
				m[c]=len(str(i))+1
			c=c+1
	s = "{0:"+str(m[0])+"} {1:"+str(m[1])+"} {2:"+str(m[2])+"} {3:"+str(m[3])+"} {4:"+str(m[4])+"}"
	for l in a:
		print s.format(l[0], l[1], l[2], l[3], l[4])


def listLocalParameters(front=DEFAULT_FRONT, back=DEFAULT_BACK, title="Titel", unit="Unit"):
	listParameter(LOCALS_PARAM_FILE,front,back,title,unit)

def listAreaParameters(front=DEFAULT_FRONT, back=DEFAULT_BACK, title="Titel", unit="Unit", color="Color"):
	f = open(AREA_PARAM_FILE,"r")
	param=[]
	if len(f.read()) != 0:
		f.seek(0)
		param = json.load(f)
		f.close()
	else:
		print EMPTY_ERROR
		f.close()
		return
	param.insert(0,[title, front, back, unit, color])
	maxlen = 0
	for front in param:
		for digit in front:
			if len(str(digit)) > maxlen:
				maxlen = len(str(digit))
	form = "{0:"+str(maxlen)+"} {1:"+str(maxlen)+"} {2:"+str(maxlen)+"} {3:"+str(maxlen)+"} {4:"+str(maxlen)+"}"
	for front in param:
		print form.format(front[0],front[3],front[1],front[2], front[4])

def listParameter(file_name, front=DEFAULT_FRONT, back=DEFAULT_BACK, title="Titel", unit="Unit"):
	f = open(file_name,"r")
	param=[]
	if len(f.read()) != 0:
		f.seek(0)
		param = json.load(f)
		f.close()
	else:
		print EMPTY_ERROR
		f.close()
		return
	param.insert(0,[title, front, back, unit])
	maxlen = 0
	for front in param:
		for digit in front:
			if len(str(digit)) > maxlen:
				maxlen = len(str(digit))
	form = "{0:"+str(maxlen)+"} {1:"+str(maxlen)+"} {2:"+str(maxlen)+"} {3:"+str(maxlen)+"}"
	for front in param:
		print form.format(front[0],front[3],front[1],front[2])

if __name__ == "__main__":
	listLocales()
	listAreas()
	listLocalParameters()
	listAreaParameters()