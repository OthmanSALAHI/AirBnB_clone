import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models import storage
import pycodestyle


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = storage
        self.base_model = BaseModel()
        self.user = User()
        self.amenity = Amenity()
        self.city = City()
        self.place = Place()
        self.review = Review()
        self.state = State()

    def tearDown(self):
        """Clean up by removing the created JSON file"""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_method(self):
        """Test if the all method returns the
        correct dictionary"""
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIs(all_objs, self.storage._FileStorage__objects)

    def test_new_method(self):
        """Test if new method adds an object to the
        storage dictionary"""
        self.storage.new(self.base_model)
        self.assertIn('BaseModel.{}'.format(self.base_model.id),
                      self.storage._FileStorage__objects)

    def test_save_method(self):
        """Test if save method correctly saves objects
        to the JSON file
        """
        self.storage.new(self.user)
        self.storage.new(self.amenity)
        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)

        self.assertIn('User.{}'.format(self.user.id), data)
        self.assertIn('Amenity.{}'.format(self.amenity.id), data)

    def test_reload_method(self):
        """Test if reload method correctly reloads
        objects from the JSON file
        """
        self.storage.new(self.city)
        self.storage.save()
        self.storage.reload()
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIn('City.{}'.format(self.city.id), all_objs)

    def test_pycodestyle(self):
        """unittest to test pycodestyle compliance"""
        style_guide = pycodestyle.StyleGuide()
        result = style_guide.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
