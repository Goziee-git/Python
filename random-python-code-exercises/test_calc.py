import unittest
import test #calc is the module we want to test so we name it test_calc.py


class TestCalc(unittest.TestCase):

   '''we creates methods for what we are testing'''

   def test_add(self):
      result = test.add(10, 5)
      self.assertEqual(result, 15)