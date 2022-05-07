# A simple Python function to demonstrate Polymorphism
# ********** polymorphic functions:****************
def add(x, y, z=0):
    return x + y+z


# Driver code
print('-------------')
print(add(3, 4))
print(add(3, 4, 5))

# ********** Polymorphism with class methods:****************


class University:
    def intro(self):
        print("Bangladesh has 53 public and 100 private universities.")

    def numberOfUniversity(self):
        print("Most of the universities are in Dhaka Division.")


class Sylhet(University):
    def numberOfUniversity(self):
        print("There are 13 universities in Sylhet Division.")


class Rajshahi(University):
    def numberOfUniversity(self):
        print("There are 18 universities in Rajshahi Division.")


obj_bird = University()
obj_spr = Sylhet()
obj_ost = Rajshahi()

print('-------------')
obj_bird.intro()
obj_bird.numberOfUniversity()

print('-------------')
obj_spr.intro()
obj_spr.numberOfUniversity()

print('-------------')
obj_ost.intro()
obj_ost.numberOfUniversity()
