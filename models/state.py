#!/usr/bin/python3
""" State Module for HBNB project """
import os

from models.base_model import BaseModel, Base

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='delete')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Returns list of cities for the current state"""
            from models import storage
            return [city
                    for city in
                    list(storage.all("City").values())
                    if city.state_id == self.id]
