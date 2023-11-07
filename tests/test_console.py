#!/usr/bin/python3
"""console test"""
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage
import unittest
import os
import sys

"""
Unittest classes:
    TestHBNBcmd_prompt
    TestHBNBcmd_quit
    TestHBNBcmd_EOF
    TestHBNBcmd_emptyline
    TestHBNBcmd_create
    TestHBNBcmd_show
    TestHBNBcmd_destroy
    TestHBNBcmd_all
    TestHBNBcmd_update
    TestHBNBcmd_count
    TestHBNBcmd_help

"""
class TestHBNBcmd_prompt(unittest.TestCase):
    """Test prompt"""

    def test_prompt(self):
        """equalizing the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Test prompt"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBcmd_quit(unittest.TestCase):
    """ test quit """
    
    def test_quit(self):
        """test the quit cmd"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))