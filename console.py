#!/usr/bin/python3
# console.py
"""Defines the AirBnb clone console."""
import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
