#!/usr/bin/python3
"""
* @file _login.py
* @description:  This module defines the login for the easycut Application

* FUNCTIONS:
    None

* CLASSES:
          class Login(BaseModel, Base):
                  The Login class will contain all the logic required for the Login that has to
                  do with a login object. It basically stores the values or attributes of a login
                  object so it can be maniplated and for easy storage and retrieval.

                  It's parent classes BaseModel and Base:
                    The BaseModel class is a class defined by us in the file basemodel.py in this directory
                    The Base class is a class gotten from the sqlalchemy module. It is needed for perfect operation
                    of the database storage.

* @author:                                  Idaewor Favour <idaeworfavour1@gmail.com>
* @creation_date:                           Friday, 18 June 2024, Idaewor Favour.
"""
import bcrypt
from datetime import datetime
import models
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Login(BaseModel, Base):
    """The Login class represents a login object that holds data obout a particular login
        The data may include last_login, login_attemps, user_id, and so on... 

        This class is needed specifically to ease development and for us to use declarative programming or ORM
        in sqlalchemy.

        Class Attributes:
            last_login: The last login timestamp of the user
            login_attempts: The number of times the user tried to login
            user_id: The id of the user whose data is being stored.

            session_token: The session token. This is for when database storage is not being used.

        Class Methods:
            def __init__(self, *args, **kwargs):
                The initialization method of the Login class.
                It initializes a login object to be created.

                It calls the __init__ method of the parent class.
        
        **Note: More documentation in the class documentation above.**
    """

    # Checks if the storage type beign used for database.
    if models.storage_t == "db":
        __tablename__ = "logins"
        last_login = Column(DateTime, default=datetime.utcnow)
        login_attempts = Column(Integer, default=0)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    else:
        user_id = ""
        login_attempts = 0
        sessionToken = ""

    def __init__(self, *args, **kwargs):
        """The Init Method of the Login class
        """
        super().__init__(*args, **kwargs)

    def validate_user(self, email, password):
        """
            The validate_user method of the Login class
        """
        # if email in models.storage.all(User).values().email:
        users = models.storage.all('User')
        for obj in users.values():
            if obj.email:
                if obj.email == email:
                    if not isinstance(obj.password, str):
                        obj.password = obj.password.decode()
                    stored_hash = obj.password.encode()
                    return bcrypt.checkpw(password.encode('utf-8'), stored_hash), obj.id
                
        # user_id = next((obj_id for obj_id, obj in models.storage.all('User').items() if obj.email == email), None)
        # print(user_id)
        # stored_hash = models.storage.get("User", user_id).password
        # # Validate password and returns True if it is correct
        # return bcrypt.checkpw(password.encode('utf-8'), stored_hash)