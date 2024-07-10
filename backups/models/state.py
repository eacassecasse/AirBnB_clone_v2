#!/usr/bin/python3
""" State Module for HBNB project """
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete-orphan')

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Returns list of cities for the current state"""
            from models import storage
            return [city
                    for city in
                    [storage.all().get(k) for k in storage.all()
                     if k.partition('.')[0] == 'City']
                    if city.state_id == self.id]
