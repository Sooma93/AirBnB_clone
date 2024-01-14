#!/usr/bin/python3
"""test file storage"""

import unittest
import pep8
import json
import inspect
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorage(unittest.TestCase):
    ''' Test File storage '''

    def test_pep8_File_Storage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Check pep8")

 def test_all_method_returns_dictionary(self):
        """test_all_method_returns_dictionary"""
        storage = FileStorage()
        obj1 = BaseModel()
        obj2 = User()
        storage.new(obj1)
        storage.new(obj2)
        result = storage.all()
        self.assertIsInstance(result, dict)
        self.assertIn(f"{obj1.__class__.__name__}.{obj1.id}", result)
        self.assertIn(f"{obj2.__class__.__name__}.{obj2.id}", result)

    # new method adds a new serialized object to the dictionary
    def test_new_method_adds_new_object(self):
        """test_new_method_adds_new_object"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        result = storage.all()
        self.assertIn(f"{obj.__class__.__name__}.{obj.id}", result)

    def test_all_method_returns_empty_dictionary(self):
        """test_all_method_returns_empty_dictionary"""
        storage = FileStorage()
        result = storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_raises_attribute_error(self):
        """test_new_method_raises_attribute_error"""
        storage = FileStorage()
        obj = "not a BaseModel instance"
        with self.assertRaises(AttributeError):
            storage.new(obj)

   def test_new(self):
        """test that new adds an object to the FileStorage.__objects attr"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        storage._FileStorage__objects = {}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

 def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "State class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


if __name__ == "__main__":
    unittest.main()
