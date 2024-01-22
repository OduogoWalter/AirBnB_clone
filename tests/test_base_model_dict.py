#!/usr/bin/python3
"""
Unit tests for BaseModel class with dictionary representation
"""
import unittest
from models.base_model import BaseModel

class TestBaseModelDict(unittest.TestCase):
    def test_from_dict(self):
        """Test creating a BaseModel instance from a dictionary"""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(str(my_model.created_at), str(my_new_model.created_at))
        self.assertEqual(str(my_model.updated_at), str(my_new_model.updated_at))
        self.assertEqual(str(my_model), str(my_new_model))

if __name__ == '__main__':
    unittest.main()
