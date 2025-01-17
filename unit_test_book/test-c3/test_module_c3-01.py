import unittest
"""the class below is the base class"""
class TestClass01(unittest.TestCase): #TestClass01 is the first class, subclassed from the testcase class of the unittest module.
   """defined below is the test fixture"""
   def test_case01(self):
      my_str = "ASHWIN"
      my_int = 999
      self.assertTrue(isinstance(my_str, str)) #assertions 
      self.assertTrue(isinstance(my_int, int)) #assertions

   def test_case02(self):
      my_pi = 3.14
      self.assertFalse(isinstance(my_pi, int))

if __name__ == '__main__':
   unittest.main()  #unittest.main() is the test runner
