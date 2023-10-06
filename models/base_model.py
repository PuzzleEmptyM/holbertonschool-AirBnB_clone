#!/usr/bin/python3
"""Defines class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Creates a new BaseModel"""

    def __init__(self):
        """Initializes an instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Creates string representation of object"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates most recent change in time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Creates dictionary representation of object"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
