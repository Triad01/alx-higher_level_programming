#!/usr/bin/python3
"""
Script takes an argument
and displays all rows in
the states table where name
matches an argument
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
         host="localhost",
         user=argv[1],
         passwd=argv[2],
         db=argv[3]
     )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s", (argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
