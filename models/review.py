#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): place id
        user_id (str): user id
        text (str): review description
    """

    place_id = ""
    user_id = ""
    text = ""
