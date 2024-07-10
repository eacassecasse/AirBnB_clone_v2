#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models

    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the storage engine"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        host = os.getenv("HBNB_MYSQL_HOST")
        env = os.getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query a return all objects from the database
        depending on the class, if the class was not provided then,
        it will return all types objects"""

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        if cls is None:
            objects = []
            for cls_type in classes.values():
                objects.extend(self.__session.query(cls_type).all())
        else:
            if isinstance(cls, str):
                cls = classes.get(cls)
            objects = self.__session.query(cls).all()

        return {"{}.{}".format(type(o).__name__, o.id): o for o in objects}

    def new(self, obj):
        """Adds new object into the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes to the database"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)

        factory = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def delete(self, obj=None):
        """ Deletes an object from the database """
        self.__session.delete(obj)

    def close(self):
        """ Closes the storage engine """
        self.__session.close()
