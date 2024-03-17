#!/usr/bin/python3
"""
This script takes in the name of a state
as an argument and lists all cities of that
state, using the database `hbtn_0e_4_usa`.
"""

import sys
import MySQLdb

def get_cities_by_state(mysql_username, mysql_password, db_name, state_name):
    """
    Retrieve cities of a given state from the database.
    """
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", user=mysql_username, port=3306,
                             passwd=mysql_password, db=db_name)

        # Create a cursor object
        with db.cursor() as cursor:
            # Execute the query
            cursor.execute("""
                SELECT cities.id, cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %(state_name)s
                ORDER BY cities.id ASC
            """, {'state_name': state_name})

            # Fetch the results
            rows = cursor.fetchall()

            # Print the cities
            for row in rows:
                print(row[1])

    except MySQLdb.Error as e:
        print(f"Error accessing database: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if db:
            # Close the database connection
            db.close()

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql_username> <mysql_password> <db_name> <state_name>")
        sys.exit(1)

    # Extract command line arguments
    mysql_username, mysql_password, db_name, state_name = sys.argv[1:]

    # Call the function to retrieve cities by state
    get_cities_by_state(mysql_username, mysql_password, db_name, state_name)

