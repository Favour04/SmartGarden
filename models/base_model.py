#!/usr/bin/python3
# BaseModel module		
import models
import uuid
from datetime import datetime

if models.storage_t == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """
    BaseModel class represents the base model for all other models in the application.

    Attributes:
        id (str): The unique identifier for the model instance.
        created_at (datetime): The timestamp indicating when the model instance was created.
        updated_at (datetime): The timestamp indicating when the model instance was last updated.

    Methods:
        __init__(self, *args, **kwargs): Initializes a new instance of the BaseModel class.
        __str__(self): Returns a string representation of the BaseModel instance.
        save(self): Saves the current state of the BaseModel instance.
        to_dict(self): Converts the BaseModel instance to a dictionary representation.

    """
    
    # Check if the storage type specified in __init__.py is database  
    if models.storage_t == "db":
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, default=datetime.now) 
        updated_at = Column(DateTime, default=datetime.now) 

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            None
        """
    
        # If kwargs is not empty, update the instance attributes with the provided values
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == 'updated_at':
                    kwargs[key] = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
            if '__class__' in kwargs:
                del kwargs['__class__']
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Saves the current state of the BaseModel instance.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """
        dict = {}
        dict.update(self.__dict__)
        dict["__class__"] = f"{self.__class__.__name__}"
        if not isinstance(dict["created_at"], str):
            dict["created_at"] = self.created_at.isoformat()
        if not isinstance(dict["updated_at"], str):
            dict["updated_at"] = self.updated_at.isoformat()
        return dict
                                                                                                                                        