#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class inherit from BaseModel
    Attributes:
        email (str): adresse email
        password (str): password
        first_name (str): first name
        last_name (str): last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
