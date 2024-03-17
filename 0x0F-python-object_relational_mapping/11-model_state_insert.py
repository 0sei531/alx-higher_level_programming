#!/usr/bin/python3
"""
This script retrieves the id of a State object by name from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

def print_usage():
    print("Usage: {} <username> <password> <database_name> <state_name>".format(argv[0]))

if __name__ == "__main__":
    if len(argv) != 5:
        print("Invalid number of arguments.")
        print_usage()
        exit(1)

    username, password, database_name, state_name = argv[1:]

    try:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database_name), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).filter_by(name=state_name).first()

        if state is None:
            print("State '{}' not found.".format(state_name))
        else:
            print("ID of state '{}': {}".format(state_name, state.id))

        session.close()

    except Exception as e:
        print("An error occurred:", e)

