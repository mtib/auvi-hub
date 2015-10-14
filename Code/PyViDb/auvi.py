#!/usr/bin/python3
"""
    _       __     ___
   / \  _   \ \   / (_)
  / _ \| | | \ \ / /| |
 / ___ | |_| |\ V / | |
/_/   \_\__,_| \_/  |_|
############################
# author: Markus Becker    #
# email: markus@tibyte.net #
# created: 14.10.2015      #
############################
"""
# This is the main Programm
# logger:
from fileio import log, error, changeSetting, getSetting
# TODO connect sqlinterface
import sqlinterface as sql
# TODO grads interface or octave?
# TODO read about source format


def main():
    info()
    log("log", "PyViDb was executed!")


def info():
    print("This is PyViDB. Switching from JSON to sqlite3")

if __name__ == '__main__':
    main()
