#!/usr/bin/python3
# console.py
"""Defines the AirBnB console."""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Set the command prompt """
    prompt = "(hbnb)"

    def do_create(self, args):
        """Creates a new object"""
        if not args:
            print("** no class name **")
            return
        if args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Shows instance based on classname and ID"""
        if not args:
            print("** no class name **")
            return
        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key in all_objects:
            print(all_objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """Destroy an object"""
        if not args:
            print("** no class name **")
            return
        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key in all_objects:
            del all_objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """Print all instances based on class name"""
        arg_list = args.split()
        if not args or arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        class_name = arg_list[0]
        all_objects = storage.all()
        obj_list = [str(obj) for key, obj in all_objects.items()
                    if key.split('.')[0] == class_name]
        print(obj_list)

    def do_update(self, args):
        """Update attributes of an object"""
        if not args:
            print("** no class name **")
            return
        arg_list = args.split()
        class_name = arg_list[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        instance_id = arg_list[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** no attribute name **")
            return
        attr_name = arg_list[2]
        if len(arg_list) < 4:
            print("** value missing **")
            return
        attr_value = arg_list[3]
        obj = all_objects[key]

        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            if attr_type == str:
                setattr(obj, attr_name, attr_value)
            elif attr_type == int:
                setattr(obj, attr_name, int(attr_value))
            elif attr_type == float:
                setattr(obj, attr_name, float(attr_value))
            obj.save()
        else:
            print("** attribute doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
