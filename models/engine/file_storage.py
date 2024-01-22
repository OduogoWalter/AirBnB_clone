#!/usr/bin/python3
"""
Module for the FileStorage class
"""
import json
from os import os
from models.base_model import BaseModel

class FileStorage:
    """
    FileStorage class that serializes
    instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with
        key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the
        JSON file (path: __file_path)
        """
        serializable_dict = {key: obj.to_dict()
                            for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w',
                  encoding='utf-8') as file:
            json.dump(serializable_dict, file)

    def reload(self):
        """
        Deserializes the JSON
        file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_dict[key] = BaseModel(**value)
                FileStorage.__objects = obj_dict
