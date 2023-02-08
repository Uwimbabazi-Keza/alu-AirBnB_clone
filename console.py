#!/usr/bin/python3
import cmd
import uuid
import datetime
import json

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name in classes:
                new_instance = classes[class_name]()
                new_instance.id = str(uuid.uuid4())
                new_instance.created_at = datetime.datetime.now()
                new_instance.updated_at = datetime.datetime.now()
                instances.append(new_instance)
                with open(class_name + ".json", "w") as file:
                    json.dump(new_instance.to_dict(), file)
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            if class_name in classes:
                instance_found = False
                for instance in instances:
                    if instance.id == instance_id and type(instance)._name_ == class_name:
                        print(instance)
                        instance_found = True
                        break
                if not instance_found:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            class_name, instance_id = args[0], args[1]
            if class_name in classes:
                instance_found = False
                for instance in instances:
                    if instance.id == instance_id and type(instance)._name_ == class_name:
                        instances.remove(instance)
                        instance_found = True
                        break
                if not instance_found:
                    print("** no instance found **")
                else:
                    with open(class_name + ".json", "w") as file:
                        json.dump([i.to_dict
