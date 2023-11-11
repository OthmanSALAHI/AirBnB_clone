#!/usr/bin/python3
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pycodestyle
from models.state import State
import models
from io import StringIO
import sys
from unittest.mock import patch


class Testthestate(unittest.TestCase):
    """test the state class"""
    def test_thestate(self):
        """test the state"""
        new = State()
        self.assertTrue(hash(new), "id")
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        """type test"""
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)


class Testcodestyle(unittest.TestCase):
    """test codestyle"""
    def test_pep8(self):
        """test pep8"""
        pyc = pycodestyle.StyleGuide(quiet=True)
        result = pyc.check_files(["models/user.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)


if __name__ == '__main__':
    unittest.main()
