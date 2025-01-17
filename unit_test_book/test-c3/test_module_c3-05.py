import unittest

def setUpModule():
   """Called once, before antthing else in this module"""
   print("In setUpModule()...")

def tearDownModule():
   """Called once, after everything else in this module"""

class TestClass06(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      """Called once, before any test"""
      print("In setUpClass()...")

   @classmethod
   def tearDownClass(cls):
      """called once, after all tests, if setUpClass Successful"""
      print("In tearDownClass()...")

   def setUp(self):
      """Called multiple times, before every test method"""
      print("\nIn setUp()...")
   def tearDown(self):
      """Called multiple times after evert test method"""
      print("in tearDown()...")

   def test_case01(self):
      self.assertTrue("PYTHON".isupper())
      print("In test_case01()")

   def test_case02(self):
      self.assertFalse("python".isupper())
      print("In test_case02()")

if __name__ == "__main__":
   unittest.main()
