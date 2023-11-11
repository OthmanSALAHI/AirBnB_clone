#!/usr/bin/python3
import json
import unittest
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import pycodestyle
import models
from io import StringIO
import sys
from unittest.mock import patch


class TestCity(unittest.TestCase):
    """ city class unit test """

    def setUp(self):
        self.city = City()
        self.city.name = "San Francisco"
        self.city.state_id = "CA"

    def tearDown(self):
        del self.city

    def test_save_reload_city(self):
        """ test that a City object can be saved and reloaded correctly """
        storage.new(self.city)
        storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        new_objects = new_storage.all()
        self.assertIn(f"City.{self.city.id}", new_objects)
        new_city = new_objects[f"City.{self.city.id}"]
        self.assertEqual(new_city.name, self.city.name)
        self.assertEqual(new_city.state_id, self.city.state_id)

    def test_reload(self):
        """ ensure that reload works """
        len_before = len(storage.all())
        storage.new(City())
        storage.reload()
        len_after = len(storage.all())
        self.assertEqual(len_after, len_before + 1)


class Testcodestyle(unittest.TestCase):
    """test codestyle"""
    def test_pep8(self):
        """test pep8"""
        pyc = pycodestyle.StyleGuide(quiet=True)
        result = pyc.check_files(["models/user.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)


class testthecity(unittest.TestCase):
    """test the city class"""
    def test_thecity(self):
        """test the city"""
        new = City()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "state_id"))
        """type test"""
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.state_id, str)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.id, str)


if __name__ == '__main__':
    unittest.main()
