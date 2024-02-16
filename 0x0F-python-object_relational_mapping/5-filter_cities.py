#!/usr/bin/python3
"""  lists all cities by state from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    filter = sys.argv[4]
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                    FROM cities
                    INNER JOIN states ON cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id""", (filter,))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
