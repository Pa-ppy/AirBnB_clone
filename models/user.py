#!/usr/bin/python3
"""
a class User that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
