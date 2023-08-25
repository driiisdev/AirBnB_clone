#!/usr/bin/python3
""" holds class User"""

from models import base_model


class User(base_model.BaseModel):
    """class User that inherits from class BaseModel"""
    """Representation of a user """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
