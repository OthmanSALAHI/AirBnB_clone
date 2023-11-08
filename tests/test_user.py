#!/usr/bin/python3
import pycodestyle
import unittest
import models
from io import StringIO
import sys


class Testpycodestyle(unittest.TestCase):
    """ test codestyle """
    def test_pycode(self):
        """ test pycodestyle """
        pycode = pycodestyle.StyleGuide(quiet=True)
        result = pycode.check_files(["models/user.py"])
        MessageErr = "code style error pr warning !"
        self.assertEqual(result.total_errors, 0, MessageErr)


if __name__ == '__main__':
    unittest.main()
