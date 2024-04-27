#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connecting to the database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         passwd=password, db=database, user=username)
    """connecting cursor"""
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = '{}'"
                .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
