#!/usr/bin/python3
"""
This script lists all cities from the database `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    # Use a context manager for the cursor to ensure proper resource cleanup
    with db.cursor() as cur:
        # Execute the SQL query to fetch cities along with their corresponding states
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        # Fetch all rows from the result set
        rows = cur.fetchall()

    # Print the results
    if rows:
        for row in rows:
            print(row)

