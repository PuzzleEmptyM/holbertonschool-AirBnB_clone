#!/usr/bin/python3
# base_model.py
"""Defines class BaseModel"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Creates new BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes new instance of BaseModel.

        Args:
            args (any): Not used
            kwargs (dict): Key/Value pairs to use as attributes
        """
        d_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, d_t)
                elif key == "__class__":
                    pass
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates most recent change in time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates dictionary representation of obj"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """Returns string representation of obj"""
        cls = self.__class__.__name__
        return "[{}] ({}) {}".format(cls, self.id, self.__dict__)
