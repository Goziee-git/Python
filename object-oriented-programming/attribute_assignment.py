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

class Books:

   books = []
   
   def __init__(self, title, author):
      self.title = title 
      self.author = author 

   def add_book(self):
      """using the if conditional statement to check if books exist"""
      if self not in Books.books:
         Books.books.append(self)
      return f"{self.title} by {self.author} has been added"

   def delete_book(self):
      if self in Books.books:
         Books.books.remove(self)

   def display_books(self):
      return [f"{book.title} by {book.author}" for book in books]
      return [f"{book.title} by {book.author}" for book in Books.books]
      
book1 = Books("The Alchemist", "Paulo Coelho")
print(book1.add_book())
book2 = Books("The 48 Laws of Power", "Robert Greene")
print(book2.add_book())
book3 = Books("The 50th Law", "Robert Greene")
print(book3.add_book())