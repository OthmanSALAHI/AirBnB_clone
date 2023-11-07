#!/usr/bin/python3
from models.base_model import BaseModel

 
class City(BaseModel):
    """ the inhreit class of BaseModel 
    Attributes:
        state_id (str): the id of state
        name (str): the name of city
    """
    state_id = ""
    name = ""
        