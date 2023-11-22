#!/usr/bin/python3
"""Lists all cities of the database hbtn_0e_4_usa, ordered by city id."""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states ON cities.state_id = states.id \
            ORDER BY states.id")
    [print(city) for city in cur.fetchall()]
