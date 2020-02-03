#!/usr/bin/python3
""" Disasters class"""

from models.disaster import Disaster
import json


class FileStorage:
    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def all(self, cls=None):
        """returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def new(self, obj):
        """Create a new object"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Add a new instance to the dictionary of objects and the save it"""
        my_dict = {}
        if len(self.__objects) > 0:
            for key, value in self.__objects.items():
                my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def get(self, place):
        """find a object by its plane name"""
        if place is None:
            return None
        else:
            self.all()
            for obj in self.__objects.values():
                if obj.place == place:
                    return obj.id
            return None

    def delete(self, obj=None):
        """
        to delete obj from __objects if it’s inside
        Args:
            obj: object that its going to be deleted
        Returns:
        """
        if obj is not None:
            obj_id = obj.id
            obj_class = obj.__class__.__name__
            key = obj_class + '.' + obj_id
            try:
                objects = self.__objects
                if key in objects:
                    del objects[key]
                    self.save()
                else:
                    raise KeyError()
            except KeyError:
                print("** no instance found **")
