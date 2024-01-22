#!/usr/bin/python3
"""
Unit tests for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        """Test initialization of BaseModel"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)

    def test_str(self):
        """Test __str__ method of BaseModel"""
        bm = BaseModel()
        self.assertEqual(str(bm),
                         "[BaseModel] ({}) {}".format(bm.id, bm.__dict__))

    def test_save(self):
        """Test save method of BaseModel"""
        bm = BaseModel()
        initial_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(initial_updated_at, bm.updated_at)

    def test_to_dict(self):
        """Test to_dict method of BaseModel"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)


if __name__ == '__main__':
    unittest.main()
