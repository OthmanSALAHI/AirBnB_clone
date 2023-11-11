#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models import storage
from datetime import datetime

""" Amenity class unit test """


class TestAmenity(unittest.TestCase):
    """ Amenity class unit test """

    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Swimming Pool"

    def test_all(self):
        """ ensure the all() method returns
        the correct dictionary of objects
        """
        all_objects = storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertIs(all_objects, storage._FileStorage__objects)

    def test_new(self):
        """ ensure new object is added to __objects dictionary """
        initial_count = len(storage.all())
        storage.new(self.amenity)
        new_count = len(storage.all())
        self.assertNotEqual(new_count, initial_count + 1)

    def test_save_reload(self):
        """
        ensure that objects are correctly
        saved and reloaded from the JSON file
        """
        storage.new(self.amenity)
        storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        new_objects = new_storage.all()
        self.assertIn(f"Amenity.{self.amenity.id}", new_objects)

    def test_reload(self):
        """ ensure that reload works """
        len_before = len(storage.all())
        storage.new(Amenity())
        storage.reload()
        len_after = len(storage.all())
        self.assertEqual(len_after, len_before + 1)


class testtheamenity(unittest.TestCase):
    """test the amenity class"""
    def test_theamenity(self):
        """test the amenity"""
        new = Amenity()
        self.assertTrue(hash(new), "id")
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))
        """type test"""
        self.assertIsInstance(new.name, str)
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
