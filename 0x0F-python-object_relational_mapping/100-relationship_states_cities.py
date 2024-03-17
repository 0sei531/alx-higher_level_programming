#!/usr/bin/python3
"""Create a State with the City “San Francisco”."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == "__main__":
    # Connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create the State "California"
    california = State(name="California")
    
    # Create the City "San Francisco" linked to "California"
    san_francisco = City(name="San Francisco", state=california)

    # Add "California" and "San Francisco" to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes
    session.commit()
    
    # Close the session
    session.close()

