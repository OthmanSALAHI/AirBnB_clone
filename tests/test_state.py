#!/usr/bin/python3
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime as dt
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
        self.assertIsInstance(new.created_at, dt)
        self.assertIsInstance(new.updated_at, dt)

class Testpycodestyle(unittest.TestCase):
    """ test codestyle """
    def test_pycode(self):
        """ test pycodestyle """
        pycode = pycodestyle.StyleGuide(quiet=True)
        result = pycode.check_files(["models/state.py"])
        MessageErr = "code style error pr warning !"
        self.assertEqual(result.total_errors, 0, MessageErr)

if __name__ == '__main__':
    unittest.main()