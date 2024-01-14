#!/usr/bin/python3
""" Test city """

import unittest
import pep8
import os
import models
from datetime import datetime
from models.city  import City
from models.base_model import BaseModel

class TestCity_instantiation(unittest.TestCase):
    """ Tests city """

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

if __name__ == "__main__":
    unittest.main()
