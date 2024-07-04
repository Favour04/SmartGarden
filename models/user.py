#!/usr/bin/python3
import bcrypt
import models
from models.base_model import BaseModel
from datetime import datetime
# from models import storage
from sqlalchemy import Column, String
import os

"""
    This Module contains the class
    User that inherits from BaseModel
"""
class User(BaseModel):
    """
        User class that inherits from BaseModel
        Attributes:
            email (str): The email of the user.
            password (str): The password of the user.
            username (str): The username of the user.
            streak (int): The streak of the user.
            leaderboard (int): The leaderboard of the user.
    """
    if models.storage_t == "db":
        __tablename__ = "users"
        username = Column(String(128), nullable=True)
        password = Column(String(128), nullable=False)
        salt = Column(String(128), nullable=True)
        email = Column(String(128), nullable=False)
    else:
        email = ""
        password = ""
        username = ""
        salt = None
        streak = 0
        leaderboard = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
    def __setattr__(self, name, value):
        """Sets a password with bycript encryption and salting."""
        if name == "password":
            # Check if salt is None, generate if needed
            if self.salt is None:
                # Generate a salt
                self.salt = bcrypt.gensalt()
            else:
            # Convert the salt from hex to bytes
                self.salt = bytes.fromhex(self.salt)
            
            # Hash the password and set the hashed value
            hashed_password = bcrypt.hashpw(value.encode('utf-8'), self.salt)
            self.salt = self.salt.hex()
            super().__setattr__(name, hashed_password)
        else:
            # For other attributes, perform standard assignment
            super().__setattr__(name, value)
