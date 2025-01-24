def get_my_class():
    from .submodule3 import MyClass
    return MyClass

class MyClass:
    def __init__(self):
        print("this is a class from the module03 of the submodule")
