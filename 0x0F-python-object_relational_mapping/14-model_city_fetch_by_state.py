#!/usr/bin/python3
"""connecting to a table and listing"""
from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[4]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State) \
            .filter(City.state_id == State.id) \
            .order_by(City.id):
        # Print the city and state information
        print("{}: ({}) {}".format(state.name, city.id, city.name))
