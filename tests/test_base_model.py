#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import pycodestyle


class TestBaseModel(unittest.TestCase):
    def test_instantiation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

    def test_constructor_with_kwargs(self):
        created_at_str = "2023-08-11T12:01:01.000001"
        updated_at_str = "2023-08-12T12:02:02.000002"
        instance = BaseModel(created_at=created_at_str,
                             updated_at=updated_at_str)
        self.assertEqual(instance.created_at.isoformat(), created_at_str)
        self.assertEqual(instance.updated_at.isoformat(), updated_at_str)

    def test_constructor_with_other_attributes(self):
        instance = BaseModel(name="TestModel", number=42)
        self.assertEqual(instance.name, "TestModel")
        self.assertEqual(instance.number, 42)

    def test_str_representation(self):
        instance = BaseModel()
        expected = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected)

    def test_save_method(self):
        instance = BaseModel()
        original_updated_at = instance.updated_at
        sleep(0.1)
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)

        key = "BaseModel." + instance.id
        with open("file.json", "r") as file:
            self.assertIn(key, file.read())

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        expected_keys = {"id", "created_at", "updated_at", "__class__"}
        self.assertEqual(set(instance_dict.keys()), expected_keys)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertEqual(instance_dict["__class__"], "BaseModel")


class Testcodestyle(unittest.TestCase):
    """test codestyle"""
    def test_pep8(self):
        """test pep8"""
        pyc = pycodestyle.StyleGuide(quiet=True)
        result = pyc.check_files(["models/user.py"])
        errorMessage = "Found code style errors (and warnings)."
        self.assertEqual(result.total_errors, 0, errorMessage)


if __name__ == "__main__":
    unittest.main()
