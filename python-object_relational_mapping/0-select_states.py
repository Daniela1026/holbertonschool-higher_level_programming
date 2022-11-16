#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    dbase = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         dbase=sys.argv[3], port=3306)

    cur = dbase.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)