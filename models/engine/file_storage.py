#!/usr/bin/python3
"""
file storage class
"""
import datetime
import json
import os


class FileStorage:

    """
    class for storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary
        """
        return FileStorage.__objects


    def new(self, obj):
        """
        sets in __objects
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj


    def save(self):
        """
        serializes __objects
        """
        with open(FileStorage.____file_path, "W", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)


    def classes(self):
        """
        return the refrencess of clasess
        """
        from models.base_model import BaseModel
        from models.User import User

        classes = {"BaseModel": BaseModel,
                "User": User,


    def reload(self):
        """
        deserializes the JSON file to
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_d = json.load(f)
            obj_d = {k: self.classes()[v["__class__"]](**v)
                    for k, v in obj_d.items()}
            FileStorage.__objects = obj_d
        

