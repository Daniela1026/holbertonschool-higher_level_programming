#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""


import sys
import MySQLdb


def main():

    if len(sys.argv) < 4:
        sys.exit(1)
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM `states` WHERE `name` LIKE BINARY "N%%";')
    records = cursor.fetchall()
    if len(records) > 0:
        print('\n'.join(str(record) for record in sorted(records)))


if __name__ == '__main__':
    main()
