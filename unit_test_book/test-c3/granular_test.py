import unittest

class TestClass005(unittest.TestCase):
   def test_case03(self):
      print("\nclassname: " + self.class.name)
      print("Running Test Method : " + inspect.stack()[0][3])

class TestClass006(unittest.TestCase):
   def test_case04(self):
      print("\nclassname: " + self.class.name)
      print("Running Test Method : " + inpect.stack()[0][3])

if __name__ == "__main__":
   