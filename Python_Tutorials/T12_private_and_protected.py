#***** Python program to demonstrate protected members ***********#
print('--------Demonstrate protected members---------')
# Creating a base class


class Base:
    def __init__(self):
        # Protected member: -- convention by prefixing the name of the member by a single underscore “_”
        self._a = 2

# Creating a derived class


class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class: ")
        print(self._a)


obj = Derived()

obj1 = Base()

# Uncommenting print(obj1.a) will raise an AttributeError. Calling protected member Outside class will result in AttributeError
# print(obj1.a)

#***** Python program to demonstrate private members ***********#
print('--------Demonstrate private members---------')

# Creating a Base class


class Base2:
    def __init__(self):
        self.b = "Abu Naser"
        # private member: -- convention by prefixing the name of the member by a double  underscore “__”
        self.__c = "Naser Sarker"

# Creating a derived class


class Derived2(Base2):
    def __init__(self):

        # Calling constructor of Base2 class
        Base2.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)


# Driver code
obj2 = Base2()
print(obj2.b)


# Uncommenting print(obj2.c) will raise an AttributeError
# print(obj2.c)

# Uncommenting obj3 = Derived() will also raise an AtrributeError as private member of base class is called inside derived class
# obj3 = Derived()
