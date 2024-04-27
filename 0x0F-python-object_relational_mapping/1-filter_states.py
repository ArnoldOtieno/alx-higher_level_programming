#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    """connecting the database"""

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(user=username, passwd=password, db=database,
                         host='localhost', port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()
