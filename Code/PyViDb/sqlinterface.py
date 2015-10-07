import sqlite3 as sql

# TODO connect logger

def connect(file):
    return sql.connect(file)

def connectRAM(file):
    return sql.connect(":memory:")

# should not be called,
# could print some info
def main():
    pass

if __name__ == '__main__':
    main()
