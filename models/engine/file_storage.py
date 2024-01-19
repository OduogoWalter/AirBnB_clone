#!/usr/bin/python3

import json
from models.base_model import BaseModel
from datetime import datetime
from os import path

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(FileStorage.__file_path, mode='w',
                  encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as file:
                serialized_objects = json.load(file)
                for key, obj_dict in serialized_objects.items():
                    class_name, obj_id = key.split('.')
                    obj_dict["created_at"] = datetime.strptime(obj_dict["created_at"],
                                                               "%Y-%m-%dT%H:%M:%S.%f")
                    obj_dict["updated_at"] = datetime.strptime(obj_dict["updated_at"],
                                                               "%Y-%m-%dT%H:%M:%S.%f")
                    obj = eval(class_name)(**obj_dict)
                    FileStorage.__objects[key] = obj
