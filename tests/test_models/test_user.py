#!/usr/bin/python3
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import pycodestyle
import models
from io import StringIO
import sys
from unittest.mock import patch


class Testcodestyle(unittest.TestCase):
    """test codestyle"""
    decf test_pep8(self):
        """test pep8"""
        pyc = pycodestyle.StyleGuide(quiet=True)
        result = pyc.check_files(["models/user.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)


if __name__ == '__main__':
    unittest.main()
