#!/usr/bin/python3
''' This module declares the Review class. '''
from models.base_model import BaseModel


class Review(BaseModel):
    ''' This class creates the Review object.
    Attr:
        place_id (str): identification of the place.
        user_id (str): identification of the user.
        text (str): text that contains the review of a user.
    '''
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        ''' Initialization of the attributes of the class and inherited. '''
        super().__init__(*args, **kwargs)

    def to_dict(self):
        ''' Create a dictionary with the attributes and add class, created at
        and updated at. '''
        dictionary = self.__dict__
        dictionary["__class__"] = __class__.__name__
        if "created_at" in dictionary and type(self.created_at) != str:
            dictionary["created_at"] = self.created_at.isoformat()
        if "updated_at" in dictionary and type(self.updated_at) != str:
            dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        ''' Define the structure to print. '''
        msg = "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)
        return msg
