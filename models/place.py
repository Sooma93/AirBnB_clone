#!/usr/bin/python3
"""
create a place class
"""


from models.base_model import BaseModel


class Place(BaseModel):
    """
    place object
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_nightm = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
