#!/usr/bin/python3
"""
console for the module
"""

import cmd
import json
from models.base_model import BaseModel
import models
import uuid
import os.path
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Goodbye!")
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        print("Goodbye!")
        return True

    def emptyline(self):
        """Called when an empty line is entered in response to the prompt"""
        pass

   def create(class_name, *args, **kwargs):
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        instance = globals()[class_name](*args, **kwargs)
        instance.save()
        print(instance.id)

    def show(class_name, id):
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if id is None:
            print("** instance id missing **")
            return
        instances = []
        with open('file.json') as f:
            instances = json.load(f)
        instance = [
            instance
            for instance in instances
            if instance['id'] == id
        ]
        if not instance:
            print("** no instance found **")
            return
        print(globals()[class_name](**instance[0]))

    def destroy(class_name, id):
        if class_name is None:
            print("** class name missing **")
            return
        if class_name not in globals():
            print("** class doesn't exist **")
            return
        if id is None:
            print("** instance id missing **")
            return
        instances = []
        with open('file.json') as f:
            instances = json.load(f)
        instances = [
            instance
            for instance in instances
            if instance['id'] != id
        ]
        with open('file.json', 'w') as f:
            f.write(json.dumps(instances))

    def all(class_name=None):
        instances = []
        with open('file.json') as f:
            instances = json.load(f)
        if class_name is not None:
            if class_name not in globals():
                print("** class doesn't exist **")
                return

if __name__ == '__main__':
    HBNBCommand().cmdloop()
