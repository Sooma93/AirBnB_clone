#!/usr/bin/python3
"""
the base model
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    the class which all class inhernt
    """
    def __init__(self, *args, **kwargs):
        """
        init attributes
        """
        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        return string
        """
        return "[{}] ({}) {}".format(
                type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values
        """
        d_dic = self.__dict__.copy()
        d_dic["__class__"] = type(self).__name__
        d_dic["created_at"] = d_dic["created_at"].isoformat()
        d_dic["updated_at"] = d_dic["updated_at"].isoformat()
        return d_dic
