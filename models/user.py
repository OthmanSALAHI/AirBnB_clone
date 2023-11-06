#!/usr/bin/python3
""" User class inherit from BaseModel """
from models.base_model import BaseModel


class user(BaseModel):
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
