#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

def main():

    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passw=sys.argv[2],
        dbase=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM `states` ORDER BY `id` ASC;')
    records = cursor.fetchall()
    if len(records) > 0:
        print('\n'.join(str(record) for record in records))
    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()