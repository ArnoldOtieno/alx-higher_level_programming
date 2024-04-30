#!/usr/bin/python3
"""Ascript that deletes objects from database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys

if __name__ == "__main__":
    """Creating database engine"""
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State):
        if state is not None:
            if "a" in state.name:
                session.delete(state)
    session.commit()
