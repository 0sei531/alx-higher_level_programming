#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Check if the correct number of command-line arguments are provided
    if len(argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        exit(1)

    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                             passwd=argv[2], db=argv[3])

        # Create a cursor object
        cur = db.cursor()

        # Execute SQL query with parameterized query to prevent SQL injection
        query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
        cur.execute(query, (argv[4],))

        # Fetch and print results
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        if cur:
            cur.close()
        if db:
            db.close()

