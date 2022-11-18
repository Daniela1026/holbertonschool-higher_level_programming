#!/usr/bin/python3
"""cities of that state, using the database hbtn_0e_4_usa"""


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
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    records = cursor.fetchall()
    print(", ".join([state[1] for state in records]))
    
    if __name__ == '__main__':
            main()
