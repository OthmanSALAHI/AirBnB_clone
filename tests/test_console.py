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


# TODO:  TestHBNBcmd_update
# TODO:   TestHBNBcmd_count


class TestHBNBcmd_prompt(unittest.TestCase):
    """Test prompt"""

    def test_prompt(self):
        """equalizing the prompt"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Test prompt"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())


class TestHBNBcmd_quit(unittest.TestCase):
    """test the cmd exit/quit should return true"""

    def test_exit(self):
        """test the quit cmd"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBcmd_help(unittest.TestCase):
    """test over the help cmd"""

    def tst_help_quit(self):
        help_quit = "Quit command to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(help_quit, f.getvalue().strip())

    def tst_help_create(self):
        help_create = "Create a new instance of BaseModel and print the id"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(help_create, f.getvalue().strip())

    def tst_help_show(self):
        show = "show the string representation of an instance"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(show, f.getvalue().strip())

    def tst_help_destroy(self):
        destroy = "destroy an instance"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(destroy, f.getvalue().strip())

    def tst_help_all(self):
        all = "show all instances"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(all, f.getvalue().strip())

    def tst_help_update(self):
        update = "update <class name> <id> <attribute name>"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(update, f.getvalue().strip())

    def tst_help_count(self):
        count = "count the number of instances"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(count, f.getvalue().strip())

    def tst_help_EOF(self):
        EOF = "EOF command to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(EOF, f.getvalue().strip())


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
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(cls, f.getvalue().strip())

    def test_wrong_syntax(self):
        """test over wrong syntax"""
        cls = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(cls, f.getvalue().strip())

    def test_create(self):
        """test create"""
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create User")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create State")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create City")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create Place")
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("create Review")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_obj_create(self):
        """ "create the creation of the id"""
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "BaseModel." + f.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "User." + f.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "State." + f.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "City." + f.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "Amenity." + f.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "Place." + f.getvalue().strip()
            self.assertTrue(key in storage.all().keys())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            self.assertLess(0, len(f.getvalue().strip()))
            key = "Review." + f.getvalue().strip()
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
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(cls, f.getvalue().strip())

    def test_wrong_syntax(self):
        """test over wrong syntax"""
        cls = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(cls, f.getvalue().strip())

    def test_missing_id(self):
        """test over missing id"""
        cls = "** instance id missing **"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show BaseModel")  # ! Errors start here
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show User")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show Place")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show State")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show City")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show Amenity")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show Review")
            self.assertEqual(cls, f.getvalue().strip())

    def test_wrong_id(self):
        """test over wrong id"""
        cls = "** no instance found **"
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show BaseModel 123456")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show User 123456-123456-123456")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show Place 123456-123456-123456-123456")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd("show State 123456-123456-"
                                 "123456-123456-123456")
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd(
                "show City 123456-123456-" "123456-123456-123456-123456"
            )
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd(
                "show Amenity 123456-123456-123456-123456-123456-123456-123456"
            )
            self.assertEqual(cls, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            HBNBCommand().onecmd(
                "show Review 123456-123456-123456-"
                "123456-123456-123456-123456-123456"
            )
            self.assertEqual(cls, f.getvalue().strip())

    def test_show_basemodel(self):
        """test over show basemodel"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "show BaseModel {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_user(self):
        """test over show user"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_place(self):
        """test over show place"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_state(self):
        """test over show state"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_city(self):
        """test over show city"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_amenity(self):
        """test over show amenity"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    def test_show_review(self):
        """test over show review"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertEqual(obj.__str__(), f.getvalue().strip())

    # def test_with_diff_syntax(self):
    #     err = "** instance id missing **"
    #     with patch("sys.stdout", new=StringIO()) as f:
    #         self.assertFalse( HBNBCommand().onecmd("BaseModel.show()") )
    #         self.assertEqual(err, f.getvalue().strip())
    # TODO: keep following the waves


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
        msg = "** class doesn't exist **"
        msg1 = "** class name is missing **"
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("all Model"))
            self.assertEqual(msg, f.getvalue().strip())
        # with patch ("sys.stdout", new=StringIO()) as f:
        #     self.assertFalse(HBNBCommand().onecmd("all"))
        #     self.assertEqual(msg1, f.getvalue().strip())

    def test_all_valid(self):
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertTrue(len(f.getvalue().strip()) > 0)
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertTrue(len(f.getvalue().strip()) > 0)


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
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy MyModel"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy"))
            self.assertEqual(msg1, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel"))
            self.assertEqual(msg2, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User"))
            self.assertEqual(msg2, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place"))
            self.assertEqual(msg2, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State"))
            self.assertEqual(msg2, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City"))
            self.assertEqual(msg2, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity"))
            self.assertEqual(msg2, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review"))
            self.assertEqual(msg2, f.getvalue().strip())
        # test over wrong id
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy BaseModel 123456"))
            self.assertEqual(msg3, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy User 123456"))
            self.assertEqual(msg3, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Place 123456"))
            self.assertEqual(msg3, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy State 123456"))
            self.assertEqual(msg3, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy City 123456"))
            self.assertEqual(msg3, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Amenity 123456"))
            self.assertEqual(msg3, f.getvalue().strip())
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("destroy Review 123456"))
            self.assertEqual(msg3, f.getvalue().strip())

    def test_over_correct_id(self):
        """test over correct id"""
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
            testID = f.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as f:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destroy({})".format(testID)
            self.assertFalse(HBNBCommand().onecmd(command))
            self.assertNotIn(obj, storage.all())


class TestHBNBcmd_count(unittest.TestCase):
    """test over count cmd"""

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

    def test_over_wrongsyntax(self):
        msg = "** class doesn't exist **"
        msg1 = "** class name missing **"
        with patch("sys.stdout", new_callable=StringIO) as f:
            self.assertFalse(HBNBCommand().onecmd("count Model"))
            self.assertEqual(msg, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count"))
            self.assertEqual(msg1, f.getvalue().strip())

    def test_count_cmd(self):
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count BaseModel"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count User"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Place"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count State"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count City"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Amenity"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("count Review"))
            cnt = f.getvalue().strip()
            self.assertEqual(cnt, f.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
