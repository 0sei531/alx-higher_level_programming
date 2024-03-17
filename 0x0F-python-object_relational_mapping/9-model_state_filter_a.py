#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

def list_states_with_letter_a(username, password, db_name):
    """
    Retrieve and display all State objects containing the letter 'a'.
    """
    try:
        # Create engine to connect to the database
        engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{db_name}', pool_pre_ping=True)

        # Create a session maker
        Session = sessionmaker(bind=engine)

        # Create a session
        with Session() as session:
            # Query State objects containing the letter 'a' and sort by id
            states = session.query(State).filter(State.name.contains('a')).order_by(State.id).all()

            # Display the results
            for state in states:
                print(f"{state.id}: {state.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: ./script.py <mysql_username> <mysql_password> <db_name>")
        exit(1)

    # Extract command line arguments
    username, password, db_name = argv[1:]

    # Call the function to list states with letter 'a'
    list_states_with_letter_a(username, password, db_name)

