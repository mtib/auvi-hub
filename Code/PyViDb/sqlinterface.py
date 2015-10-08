import sqlite3 as sql
import fileio

# TODO connect logger

def connect(file):
    return sql.connect(file)

def connectRAM(file):
    return sql.connect(":memory:")

def fillDatabase():
    cities = open(fileio.getSetting("dir")+fileio.getSetting("sqldir")+fileio.getSetting("citiessql"), "r")
    conn = sql.connect(fileio.getSetting("dir")+"database.db")
    c = conn.cursor()
    c.execute(cities.read())
    cities.close()
    conn.commit()
    conn.close()

# should not be called,
# could print some info
def main():
    pass

if __name__ == '__main__':
    main()
