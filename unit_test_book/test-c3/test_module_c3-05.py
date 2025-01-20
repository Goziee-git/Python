import unittest

def setUpModule():
   """Module level Fixtures"""
   print("done first, before test runs")

def tearDownModule():
   """Module level fixture for tearing down. called once after all in the module"""

class Testclass(unittest.TestCase):
   @classmethod
   def setUpClass(cls):
      """Class-Level Test Fixtures
      called once before any test"""

   @classmethod
   def tearDownClass(cls):
      """Class-Level tear down test fixtures"""


   def setUp(self):
      """Method-Level setup fixtures"""


   def tearDown(self):
      """Method-Level tear down fixtures"""


   def test_case01(self):
      self.assertTrue("PYTHON".isupper())
      print("in test_case01()")


   def test_case02(self):
      self.assertFalse("PYTHON".islower())
      print("in test_case02()")      


if __name__ == "__main__":
   unittest.main()
 


