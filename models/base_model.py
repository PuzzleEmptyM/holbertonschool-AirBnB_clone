#!/usr/bin/python3
<<<<<<< HEAD
"""Defines class BaseModel"""
=======
"""Defines the BaseModel class."""
>>>>>>> c927c9acc2d6fdcd8be3a17ce9dc5e57f81ee7b5
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes new instance of BaseModel.

        Args:
            args (any): Not used
            kwargs (dict): Key/Value pairs to use as attributes
        """
        d_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
<<<<<<< HEAD
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, d_t)
                else:
                    self.__dict__[key] = value
=======
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
>>>>>>> c927c9acc2d6fdcd8be3a17ce9dc5e57f81ee7b5
        else:
            models.storage.new(self)

    def save(self):
<<<<<<< HEAD
        """Updates most recent change in time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates dictionary representation of obj"""
=======
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
>>>>>>> c927c9acc2d6fdcd8be3a17ce9dc5e57f81ee7b5
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
<<<<<<< HEAD
        """Returns string representation of obj."""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
=======
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
>>>>>>> c927c9acc2d6fdcd8be3a17ce9dc5e57f81ee7b5
