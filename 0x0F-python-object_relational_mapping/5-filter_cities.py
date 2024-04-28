#!/usr/bin/python3
"""listing all cities"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    pword = sys.argv[4]

    """Connecting the database"""
    db = MySQLdb.connect(user=username, port=3306,
                         passwd=password, db=database, host='localhost')
    """connecting cursor"""
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    rows = cur.fetchall()
    print(", ".join([ct[2] for ct in rows if ct[4] == pword]))
    db.close()
