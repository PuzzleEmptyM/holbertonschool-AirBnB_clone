#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BaseModel class."""
=======
"""Defines class BaseModel"""
import models
>>>>>>> 3a6a815eaccbb00f224a300022da9bd83146e369
from uuid import uuid4
from datetime import datetime
import models
models.storage = {}


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
<<<<<<< HEAD
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, tform))
=======
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, d_t)
>>>>>>> 3a6a815eaccbb00f224a300022da9bd83146e369
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
<<<<<<< HEAD
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
=======
        """Updates most recent change in time."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates dictionary representation of obj"""
>>>>>>> 3a6a815eaccbb00f224a300022da9bd83146e369
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
<<<<<<< HEAD
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
=======
        """Returns string representation of obj."""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
>>>>>>> 3a6a815eaccbb00f224a300022da9bd83146e369
