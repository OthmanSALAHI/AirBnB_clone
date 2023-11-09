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


class TestHBNBcmd_create(unittest.TestCase):
    """test over the cmd create"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_missing_classname(self):
        """test over class name"""
        cls = "** class name missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create")
            self.assertEqual(cls, output.getvalue().strip())

    def test_wrong_syntax(self):
        """test over wrong syntax"""
        cls = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(cls, output.getvalue().strip())

    def test_create(self):
        """test create"""
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create User")
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create State")
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create City")
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create Amenity")
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create Place")
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("create Review")
            self.assertTrue(len(output.getvalue().strip()) > 0)

    def test_obj_create(self):
        """ "create the creation of the id"""
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "BaseModel." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "User." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "State." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "City." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "Amenity." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "Place." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            key = "Review." + output.getvalue().strip()
            self.assertTrue(key in storage.all().keys())

class HBNBcmd_show(unittest.TestCase):
    """test over the cmd show"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_missing_classname(self):
        """test over class name"""
        cls = "** class name missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show")
            self.assertEqual(cls, output.getvalue().strip())

    def test_wrong_syntax(self):
        """test over wrong syntax"""
        cls = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(cls, output.getvalue().strip())

    def test_missing_id(self):
        """test over missing id"""
        cls = "** instance id missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show BaseModel")  # ! Errors start here
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show User")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show Place")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show State")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show City")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show Amenity")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show Review")
            self.assertEqual(cls, output.getvalue().strip())

    def test_wrong_id(self):
        """test over wrong id"""
        cls = "** no instance found **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show BaseModel 123456")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show User 123456-123456-123456")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show Place 123456-123456-123456-123456")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd("show State 123456-123456-"
                                 "123456-123456-123456")
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd(
                "show City 123456-123456-" "123456-123456-123456-123456"
            )
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd(
                "show Amenity 123456-123456-123456-123456-123456-123456-123456"
            )
            self.assertEqual(cls, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            HBNBCommand().onecmd(
                "show Review 123456-123456-123456-"
                "123456-123456-123456-123456-123456"
            )
            self.assertEqual(cls, output.getvalue().strip())

    def test_show_basemodel(self):
        """test over show basemodel"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "show BaseModel {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_user(self):
        """test over show user"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_place(self):
        """test over show place"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_state(self):
        """test over show state"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_city(self):
        """test over show city"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_amenity(self):
        """test over show amenity"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_review(self):
        """test over show review"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())



class TestHBNBCommand_all(unittest.TestCase):
    """test the all cmd"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
    def test_all_invalid(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Model"))
            self.assertEqual("** class doesn't exist **", output.getvalue().strip())
    def test_all_valid(self):
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertTrue(len(output.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertTrue(len(output.getvalue().strip()) > 0)

class TestHBNBcmd_destroy(unittest.TestCase):
    """test over destroy cmd"""

    @classmethod
    def setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def down(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
    def invalid_syntax_and_value(self):
        """test over wrong syntax"""
        msg = "** class doesn't exist **"
        msg1 = "** class name missing **"
        msg2 = "** instance id missing **"
        msg3 = "** no instance found **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(msg, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(msg1, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(msg2, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(msg2, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(msg2, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(msg2, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(msg2, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(msg2, output.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(msg2, output.getvalue().strip())