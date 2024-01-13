#!/usr/bin/python3
"""
to test the file modules/base_model.py
classes:
    testbasemodel_ instnation
    test basemodel_save
    testbasemodel_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """
    to test instantiaion for the base model
    """
    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_args_unused(self):
        bs = BaseModel(None)
        self.assertNotIn(None, bs.__dict__.values())
