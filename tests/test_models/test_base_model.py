#!/usr/bin/python3
"""
Tests
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
class testBasemodel(unittest.TestCase):
        """checks every property of an instance"""
        
        model = BaseModel()
        def test_instance(self):
            self.model.name = "first model"
            self.model.number = 1
            model_json = self.model.to_dict()
            self.assertEqual(self.model.name, model_json['name'])
            self.assertEqual(self.model.number, model_json['number'])
            self.assertEqual('BaseModel', model_json['__class__'])
            self.assertEqual(self.model.id, model_json['id'])
        
        def test_save(self):
            """test save()"""
            self.model.save()
            self.assertNotEqual(self.model.created_at,self.model.updated_at)

    
                
if __name__ == '__main__':
    unittest.main()
