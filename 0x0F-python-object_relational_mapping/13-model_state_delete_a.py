#!/usr/bin/python3
"""
Write a script that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    # Create the database engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    
    # Create all tables in the engine
    Base.metadata.create_all(engine)
    
    # Create a sessionmaker bound to the engine
    Session = sessionmaker(bind=engine)
    
    # Create a session
    session = Session()
    
    try:
        # Query for all State objects whose name contains 'a'
        states_with_a = session.query(State).filter(
            State.name.ilike('%a%')).all()
        
        # Delete the State objects
        for state in states_with_a:
            session.delete(state)
        
        # Commit the changes
        session.commit()
        print("Deletion completed successfully.")
    except Exception as e:
        # Rollback the session in case of an exception
        session.rollback()
        print("An error occurred during deletion:", str(e))
    finally:
        # Close the session
        session.close()

