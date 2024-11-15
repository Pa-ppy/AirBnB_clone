#!/usr/bin/python3
"""
Unittest for FileStorage class.
"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.test_file = "test_file.json"
        FileStorage._FileStorage__file_path = self.test_file
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Tear down test environment"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all(self):
        """Test the all() method"""
        self.assertEqual(self.storage.all(), {})
        new_model = BaseModel()
        self.storage.new(new_model)
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, self.storage.all())

    def test_new(self):
        """Test the new() method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], new_model)

    def test_save(self):
        """Test the save() method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        with open(self.test_file, "r") as file:
            data = json.load(file)
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, data)

    def test_reload(self):
        """Test the reload() method"""
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, self.storage.all())
        self.assertIsInstance(self.storage.all()[key], BaseModel)


if __name__ == "__main__":
    unittest.main()
