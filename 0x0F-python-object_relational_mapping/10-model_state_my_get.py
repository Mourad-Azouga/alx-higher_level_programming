#!/usr/bin/python3
"""
Contains State class and Base, an instance of declarative_base()
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    filter = sys.argv[4]
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    the_filter = session.query(State).filter(State.name == (filter,))
    try:
        print(the_filter[0].id)
    except IndexError:
        print("Not found")
