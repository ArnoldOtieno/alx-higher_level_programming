#!/usr/bin/python3
"""search for a specific name"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    pword = sys.argv[4]

    """Connecting to the database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         passwd=password, db=database, user=username)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = '{}'"
                .format(pword))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    db.close()
