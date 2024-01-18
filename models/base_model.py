#!/usr/bin/python3
"""
Module containing the BaseModel class
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    Base class for all AirBnB objects
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel class
        """
        if kwargs:
            for key, vlaue in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value,
                                                  "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
