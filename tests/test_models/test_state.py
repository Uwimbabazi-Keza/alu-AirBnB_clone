#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.state import State

"""tests for class State"""

class test_state(unittest.TestCase):
    
    def test_init(self):
        """tests"""
        state = State()
        state.name = "Eastern Cape"
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "Eastern Cape")
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        
if __name__ == "__main__":
    unittest.main()
