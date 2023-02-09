#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class testBasemodel(unittest.TestCase):
        """checks every property of an instance"""
	
        model = BaseModel()
        def test_instance(self):
		
                self.model.name = "first model"
                self.model.number = 1
                self.model.save()
                model_json = self.model.to_dict()

                self.assertEqual(self.model.name, model_json['name'])
                # self.assertEqual(self.model.my_number, model_json['number'])
                self.assertEqual('BaseModel', model_json['__class__'])
                self.assertEqual(self.model.id, model_json['id'])

if __name__ == '__main__':
    unittest.main()