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
class TestHBNBcmd_EOF(unittest.TestCase):
    def test_EOF(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

class TestHBNBcmd_help(unittest.TestCase):
    """test over the help cmd"""

    def tst_help_quit(self):
        help_quit = "Quit command to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(help_quit, output.getvalue().strip())

    def tst_help_create(self):
        help_create = "Create a new instance of BaseModel and print the id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help create")
            self.assertEqual(help_create, output.getvalue().strip())

    def tst_help_show(self):
        show = "show the string representation of an instance"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help show")
            self.assertEqual(show, output.getvalue().strip())

    def tst_help_destroy(self):
        destroy = "destroy an instance"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(destroy, output.getvalue().strip())

    def tst_help_all(self):
        all = "show all instances"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help all")
            self.assertEqual(all, output.getvalue().strip())

    def tst_help_update(self):
        update = "update <class name> <id> <attribute name>"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help update")
            self.assertEqual(update, output.getvalue().strip())

    def tst_help_count(self):
        count = "count the number of instances"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help count")
            self.assertEqual(count, output.getvalue().strip())

    def tst_help_EOF(self):
        EOF = "EOF command to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(EOF, output.getvalue().strip())

            self.assertTrue(HBNBCommand().onecmd("create BaseModel"))