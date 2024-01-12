#!/usr/bin/python3
"""
create user class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    city objects
    """
    state_id = ""
    name = ""
