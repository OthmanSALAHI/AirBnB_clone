#!/usr/bin/python3
""" define FileStorage class. """

import json
from pathlib import Path
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


class FileStorage:
    """ storage class it's responsible for processing then storing data """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ add new object to dictionary __objects """
        object_name = obj.__class__.__name__
        FileStorage.__objects[f"{object_name}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects and writes it to json file path"""
        # Convert each object in __objects
        # to a dictionary using to_dict() method.
        new_obj_dict = {}
        for keys in FileStorage.__objects.keys():
            new_obj_dict[keys] = FileStorage.__objects[keys].to_dict()
        # Write the dictionary of objects to the JSON file.
        with open(FileStorage.__file_path, "w") as file:
            json.dump(new_obj_dict, file, indent=4)

    def reload(self):
        """ deserializes the JSON file in __file_path to __objects """
        if Path(FileStorage.__file_path).exists():
            with open(FileStorage.__file_path,
                      mode="r", encoding="utf-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name)(**value)
        else:
            return
