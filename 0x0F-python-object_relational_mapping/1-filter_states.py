#!/usr/bin/python3
"""listing names starting in 'N'"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Connecting the database"""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    [print(state) for state in cur.fetchall() if state[1][0] == "N"]


    db.close()
