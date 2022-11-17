#!/usr/bin/python3
"""all values in the states table of hbtn_0e_0_usa where name
matches the argument"""


import sys
import MySQLdb


def main():

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s", (
        sys.argv[4], ))
    records = cursor.fetchall()
    for rec in records:
        print(rec)

        cursor.close()
        db.close()

if __name__ == '__main__':
    main()
