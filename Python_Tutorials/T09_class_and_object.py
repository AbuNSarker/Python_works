# A Sample class Python program with init method
class Student:
    # Sample class attribute
    attr = "student"            # Class Variable

    # init method or constructor
    # In Python the __init__() method is called the constructor and is always called when an object is created.  The __init__ method is similar to constructors in C++ and Java.
    # The self is  is similar to this pointer in C++ and this reference in Java. If we have a method which takes no arguments, then we still have to have one argument.
    def __init__(self):
        print('Student object created!!!')

    # Adds an instance variable
    def setName(self, name):
        self.name = name       # Instance Variable

    # Adds an instance variable
    def setAge(self, age):
        self.age = age        # Instance Variable

    # Retrieves instance variable
    def info(self):
        print("I'm a", self.attr)
        print("My name is", self.name)
        print("I am ", self.age, "years old.")

    # Deleting (Calling destructor) -- The __del__() method is a known as a destructor method in Python.
    def __del__(self):
        print('Destructor called, Student object deleted.')


# Objects of Student class
S1 = Student()
S1.setName("Azim")
S1.setAge(30)
# Accessing class attributes and method through objects
S1.info()
del S1

print('---------------------')


def Create_obj():
    print('Creating Object in this function.')
    obj = Student()
    print('Function end...')
    return obj


obj = Create_obj()
print('Program End...')
