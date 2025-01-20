class Name:
   def fullname(self):
      return self.firstname + " " + self.lastname
#instance of the class Name
NorthernName = Name()
"""The attribute firstname, lastname were not assigned anywhere within the class
but dynamically assigned in the line below"""
NorthernName.firstname, NorthernName.lastname = "Jamilu", "Hassan"
print(NorthernName.fullname())
"""dynamic assignment of attributes is not great python because 
1. Lack if initialization using the __init__method to declare the class variables globally
2. Lack of ease of readability and maintainability
3. Break Type safety, introduced when using using tools like mypy
"""
print(" ................ ")
#using the __init__method for global assignmnet within the class
class Name:
   """Attributes of the Name class assigned globally"""
   def __init__(self, firstname, lastname):
      self.firstname = firstname
      self.lastname = lastname

   def ethnicname(self):
      return self.firstname + " " + self.lastname

"""instance of the class Name"""
Northerner = Name("Jamilu", "Hasssan")
print(Northerner.ethnicname())
Easterner = Name("chibuba", "amarachukwu")
print(Easterner.ethnicname())
Westerner = Name("Olusegun", "Tomisin")
print(Westerner.ethnicname())
Southerner = Name("Onisodumenya", "Hamilton")
print(Southerner.ethnicname())

print( " ............ ")
#using the dataclass module can also help with global attribute assignment
from dataclasses import dataclass

@dataclass
class Rectangle:
    length: float
    width: float

    def area(self) -> float:
        return self.length * self.width

r = Rectangle(13, 8)
print(r.area())  # Output: 104


##a random example of class
print("  ........... ")

books = []

class Books:
   def __init__(self, title, author):
      self.title = title 
      self.author = author 

   def add_book(self):
      """using the if conditional statement to check if books exist"""
      if self not in books:
         books.append(self)
      return self.title + " " + self.author

   def delete_book(self):
      if self in books:
         books.remove(self)
      return f"{self.title} by {self.author} has been removed."

# Removed reassignment of methods



Novels = Books("A Land of Power", "Johnas Audrey")
print(Novels.add_book())
print(books)
Academic_articles = Books("Programming Paradigms", "sanjay greg")
print(Academic_articles.add_book())
print(books)
print(Novels.delete_book())
