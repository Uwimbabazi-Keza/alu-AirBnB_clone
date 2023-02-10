#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__+ "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(json_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="UTF8") as file:
                data = json.load(file)
                for key, value in data.items():
                    self._objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
