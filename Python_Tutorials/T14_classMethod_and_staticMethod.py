# Python program to demonstrate use of class method and static method.

# NOTE - differences between Classmethod and StaticMehtod
# Class Method
# The class method takes cls (class) as first argument.
# Class method can access and modify the class state.
# The class method takes the class as parameter to know about the state of that class.
# @classmethod decorator is used here.

# Static Method
# The static method does not take any specific parameter.
# Static Method cannot access or modify the class state.
# Static methods do not know about class state. These methods are used to do some utility tasks by taking some parameters.
# @staticmethod decorator is used here.

from datetime import date as dt


class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def isAdult(age):
        if age > 18:
            return True
        else:
            return False

    @classmethod
    def emp_from_year(emp_class, name, year):
        return emp_class(name, dt.today().year - year)

    def __str__(self):
        return 'Employee Name: {} and Age: {}'.format(self.name, self.age)


e1 = Employee('Dhiman', 25)
print(e1)

e2 = Employee.emp_from_year('Subhas', 1987)
print(e2)

print(Employee.isAdult(25))
print(Employee.isAdult(16))
