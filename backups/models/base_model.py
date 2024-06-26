#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        server_default=text('CURRENT_TIMESTAMP'))

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            created = kwargs.get('created_at', '')
            updated = kwargs.get('updated_at', '')

            kwargs['updated_at'] = datetime.strptime(
                updated, '%Y-%m-%dT%H:%M:%S.%f') if updated else datetime.now()
            kwargs['created_at'] = datetime.strptime(
                created, '%Y-%m-%dT%H:%M:%S.%f') if updated else datetime.now()
            kwargs.pop('__class__', ' ')
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def __repr__(self):
        """ Returns a string representation of the Model """
        return self.__str__()

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                           (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            dictionary.pop('_sa_instance_state', '')
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
