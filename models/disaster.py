#!/usr/bin/python3
""" Base model class"""
import uuid
import models
from datetime import datetime


class Disaster:
    def __init__(self, **kwargs):
        """Instantiation of base model class
        Args:
            args: it won't be used
            kwargs: arguments for the constructor of the BaseModel
        Attributes:
            id: unique id generated
            created_at: creation date
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                if kwargs.get("id", None) is None:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

    def save(self):
        """Call the  new method and save method from FileStorage"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance:
        :param self:
        :return: my_dict
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict['created_at'].isoformat()
        return my_dict

