import unittest
import inspect
"""the purpose of this code is to demonstrate that we can have more than one test class"""
class TestClass04(unittest.TestCase):
   def test_case01(self):
      print("\nClassname : " + self.__class__.__name__)
      print("RUNNING TEST METHOD : " + inspect.stack()[0][3])

   
class TestClass05(unittest.TestCase):
   def test_case01(self):
      print("\nClassname : " + self.__class__.__name__)
      print("RUNNING TEST METHOD : " + inspect.stack()[0][3])

if __name__ == '__main__':
   unittest.main(verbosity=3)