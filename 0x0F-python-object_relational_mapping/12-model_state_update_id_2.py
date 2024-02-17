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
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_inst = session.query(State).filter_by(id=2).first()
    new_inst.name = 'New Mexico'
    session.commit()
