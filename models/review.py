#!/usr/bin/python3
"""
crate review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    review object
    """
    place_id = ""
    user_id = ""
    text = ""
