#!/usr/bin/python3
"""
* @file signup.py
* @description:  This module defines the signup for the Application

* FUNCTIONS:
    None

* CLASSES:
          class SignUp(BaseModel, Base):
                  The SignUp class will contain all the logic required for the SignUp that has to
                  do with a signup object. It basically stores the values or attributes of a signup
                  object so it can be maniplated and for easy storage and retrieval.

                  It's parent classes BaseModel and Base:
                    The BaseModel class is a class defined by us in the file basemodel.py in this directory
                    The Base class is a class gotten from the sqlalchemy module. It is needed for perfect operation
                    of the database storage.

* @author:                                  Idaewor Favour <idaeworfavour1@gmail.com>
* @creation_date:                           Monday, 17th June 2024, Idaewor Favour
"""
import models
from models.base_model import BaseModel, Base
from models.user import User
from sqlalchemy import Column, String

class SignUp(BaseModel, Base):
    """The SignUp class represents a signup object that holds data obout a particular signup
        The data may include first_name, password and so on...

        This class is needed specifically to ease development and for us to use declarative programming or ORM
        in sqlalchemy.

        Class Attributes:
            name = the name of the new user
            password = the password of the new user
            email = the email of the new user
            terms_and_cond = terms and conditions

        Class Methods:
            def __init__(self, *args, **kwargs):
                The initialization method of the SignUp class.
                It initializes a signup object to be created.

                It calls the __init__ method of the parent class.

        **Note: More documentation in the class documentation above.**
    """
    if models.storage_t == "db":
        __tablename__ = 'signup'
        name = Column(String(128), nullable=True)
        password = Column(String(128), nullable=False)
        email = Column(String(128), nullable=False)        
    else:
        name = ""
        password = ""
        email = ""

    def __init__(self, *args, **kwargs):
        """The Init Method of the SignUp class
        """
        super().__init__(*args, **kwargs)

    def create_user(self):
        """
            The create_user method of the SignUp class
        """
        new_user = User()
        new_user.email = self.email
        new_user.password = self.password
        new_user.save()
        return new_user