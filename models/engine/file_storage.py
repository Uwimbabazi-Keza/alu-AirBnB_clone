#!/usr/bin/python3
import json
from models.base_model import BaseModel
# from models.amenity import Amenity
# from models.city import City
# from models.place import Place
# from models.review import Review
# from models.state import State
# from models.user import User

class FileStorage:
    FILE_PATH = "file.json"
    __objects = {}

    def all(self) -> dict:
        return self.__objects

    def new(self, obj: BaseModel):
        key = obj._class.__name_ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.FILE_PATH, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        try:
            with open(self.FILE_PATH, "r", encoding="UTF8") as f:
                data = json.load(f)
                self._objects = {key: eval(value["__class_"])(**value) for key, value in data.items()}
        except FileNotFoundError:
            pass
