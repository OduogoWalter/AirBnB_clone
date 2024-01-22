#!/usr/bin/python3
"""
Module containing the BaseModel class.
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    The BaseModel class for common attributes/methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, 'update_at', datetime.now())
        else:
            setattr(self, 'id', str(uuid.uuid4()))
            setattr(self, 'created_at', datetime.now())
            setattr(self, 'updated_at', datetime.now())
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string in the format
            "[<class name>] (<self.id>) <self.__dict__>".
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute
        updated_at with the current datetime.
        """
        setattr(self, 'updated_at', datetime.now())
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
        keys/values of __dict__ of the instance.

        Returns:
            dict: A dictionary representation of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
