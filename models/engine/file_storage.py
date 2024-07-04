#!/usr/bin/phyton3
import json
import models
from models.base_model import BaseModel
from models._signup import SignUp
from models.user import User
from models._login import Login
from models.garden import Garden
classes = {"Basemodel": BaseModel, "Login": Login, "SignUp": SignUp, "User": User, "Garden": Garden}

class FileStorage:
    
    """FileStoge is a model to store data in files as json string to
    a json file.json"""

   #string - path to json file
    __file_path = "file.json"

   #dict - object is an empty dict that will contain all objects
    __objects = {}

    def all(self, clsname=None):
       """all returns all the object in the dict object"""
       if clsname is not None:
           new_dict = {}
           for key, value in self.__objects.items():
               if clsname == value.__class__ or clsname == value.__class__.__name__:
                   new_dict[key] = value
           return new_dict
       return self.__objects

    def new(self, obj):
        """set in __objects the obj with the key <obj class
        name>.id"""

        if obj is not None:
            key = f"{obj.__class__.__name__}" + "." + f"{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """serilizes __objects to the json file (path: __fil
        e_path)"""
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = self.__objects[key].to_dict()
            if value.__class__.__name__ == 'User':
                if isinstance(value.password, bytes):
                    json_objects[key]['password'] = value.password.decode()
        
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)
    
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as file:
                jsnobj = json.load(file)
            for key, value in jsnobj.items():
                self.__objects[key] = classes[value["__class__"]](**jsnobj[key])

        except Exception as err:
            print(err)
    
    def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.keys():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())
        
        return count
    