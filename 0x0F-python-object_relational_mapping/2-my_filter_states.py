#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa
Where the name is searchable by the 4th argv"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    filter = sys.argv[4]
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE  BINARY '{}'
                ORDER BY states.id""".format(filter))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
