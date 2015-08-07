import os

#Herstellen der Ordnerstruktur & evtl. Download der Dateien.
aptget = ["grads","imagemagick"]

def install():
	for prog in aptget:
		os.system("sudo apt-get install "+prog)

if __name__ == "__main__":
	install()