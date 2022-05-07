# NOTE: Inheritance is the capability of one class to derive or inherit the properties from another class. The benefits of inheritance are:
#  1. It represents real-world relationships well.
#  2. It provides reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
#  3. It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.


# **************** A Python program to demonstrate inheritance ***************
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

    # Here we return true
    def isEmployee(self):
        return True


# Driver code
print('---------------------')
emp = Person("Rasel 1")  # An Object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Rasel 2")  # An Object of Employee
print(emp.getName(), emp.isEmployee())


# ************* Python code to demonstrate multiple inheritance****************
class Base1(object):
    def __init__(self):
        self.str1 = "Azim-1"
        print("Base1")


class Base2(object):
    def __init__(self):
        self.str2 = "Azim-2"
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


print('---------------------')
ob = Derived()
ob.printStrs()


# ******************* A Python program to demonstrate inheritance **************
class Base(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name


# Inherited or Sub class (Note Person in bracket)
class Child(Base):

    # Constructor
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age

    # To get name
    def getAge(self):
        return self.age

# Inherited or Sub class (Note Person in bracket)


class GrandChild(Child):

    # Constructor
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    # To get address
    def getAddress(self):
        return self.address


# Driver code
g = GrandChild("Rony", 30, "Dhaka")
print('---------------------')
print(g.getName(), g.getAge(), g.getAddress())
