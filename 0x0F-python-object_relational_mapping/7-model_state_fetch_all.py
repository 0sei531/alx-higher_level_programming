#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_all_states(mysql_username, mysql_password, db_name):
    """
    Retrieve and display all State objects from the database.
    """
    try:
        # Create engine to connect to the database
        engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{db_name}')

        # Create a session maker
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query all State objects and sort by id
        states = session.query(State).order_by(State.id).all()

        # Display the results
        for state in states:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <db_name>")
        sys.exit(1)

    # Extract command line arguments
    mysql_username, mysql_password, db_name = sys.argv[1:]

    # Call the function to list all states
    list_all_states(mysql_username, mysql_password, db_name)

