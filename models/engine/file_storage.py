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


    def 

