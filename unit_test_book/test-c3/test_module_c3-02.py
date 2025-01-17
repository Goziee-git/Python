import unittest
import inspect
class TestClass02(unittest.TestCase):
   def test_case02(self):
      '''the inspect.stack method prints the name of the current test method.'''
      print("\nRUNNING TEST METHOD : " + inspect.stack()[0][3])
   
   def test_case01(self):
      print("\nRUNNING TEST METHOD : " + inspect.stack()[0][3])

if __name__ == '__main__': #always make sure that this block is outside the test class
   unittest.main(verbosity=2)