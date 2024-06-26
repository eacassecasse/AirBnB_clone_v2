#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import json
import os
from collections import defaultdict

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base


class DBStorage:
    """This class manages storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the storage engine"""
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        db = os.getenv("HBNB_MYSQL_DB")
        host = os.getenv("HBNB_MYSQL_HOST", default='localhost')
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

        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        if cls:
            if isinstance(cls, str):
                cls = classes.get(cls)
            return self.__session.query(cls).all() if cls else {}

        _instances = {}

        for _cls, _type in classes.items():
            _instances.update(
                        {"{}.{}".format(type(_obj).__name__, _obj.id):
                             _obj for _obj in self.__session.query(_cls)})

        return _instances

    def new(self, obj):
        """Adds new object into the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all the changes to the database"""
        self.__session.commit()

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.create_all(self.__engine)

        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def delete(self, obj=None):
        """ Deletes an object from the database """
        if obj:
            self.__session.delete(obj)

    def close(self):
        """ Closes the storage engine """
        self.__session.close()
