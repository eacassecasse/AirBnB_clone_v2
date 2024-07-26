#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
                      Column(
                          'place_id',
                          String(60),
                          ForeignKey('places.id'),
                          nullable=False,
                          primary_key=True),
                      Column(
                          'amenity_id',
                          String(60),
                          ForeignKey('amenities.id'),
                          nullable=False,
                          primary_key=True)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        amenity_ids = []

        @property
        def reviews(self):
            """ Returns list of reviews for the current place"""
            from models import storage
            return [review
                    for review in
                    [storage.all().get(k) for k in storage.all()
                     if k.partition('.')[0] == 'Review']
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """ Returns list of amenities for the current place"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """ Adds a new amenity id into the list of ids"""
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
    else:
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False)
