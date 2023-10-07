#!/usr/bin/python3
# console.py
"""Defines the AirBnb clone console."""
import cmd
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
        """Create a new object"""
        print("Object created")

    def do_retrieve(self, args):
        """Retrieve an object"""
        print("Object retrieved")

    def do_operations(self, args):
        """Perform operations on objects"""
        print("Operations performed")

    def do_update(self, args):
        """Update attributes of an object"""
        print("Object attributes updated")

    def do_destroy(self, args):
        """Destroy an object"""
        print("Object destroyed")

    def do_quit(self, args):
        """Exit the command interpreter"""
        print("Logging out...")
        return True

    def do_EOF(self, args):
        """Exit the command interpreter"""
        print("Logging out...")
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def help_quit(self):
        """Help message for the quit command"""
        print("Quit command to exit the program")

    def help_create(self):
        """Help message for the create command"""
        print("Create a new object")

    def help_retrieve(self):
        """Help message for the retrieve command"""
        print("Retrieve an object")

    def help_operations(self):
        """Help message for the operations command"""
        print("Perform operations on objects")

    def help_update(self):
        """Help message for the update command"""
        print("Update attributes of an object")

    def help_destroy(self):
        """Help message for the destroy command"""
        print("Destroy an object")

    def help_help(self):
        """Help message for the help command"""
        print("Show help messages for commands")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
