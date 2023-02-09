#!/usr/bin/python3
import uuid
from datetime import datetime

"""
Create class BaseModel that  defines all common
attributes/methods for other classes
"""
class BaseModel:
    def __init__(self, *args, **kwargs):
    self.id = str(uuid.uuid4()) if "id" not in kwargs else kwargs["id"]
    self.created_at = datetime.now()
    self.updated_at = self.created_at
    for key, value in kwargs.items():
        if key == "created_at" or key == "updated_at":
            setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            setattr(self, key, value)


    def __str__(self):
        """returns string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current datetime """
        self.save = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        dictionary = self.__dict__.copy()
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary.update({"created_at": self.created_at.isoformat()})
        dictionary.update({"updated_at": self.updated_at.isoformat()})
        return (dictionary)
