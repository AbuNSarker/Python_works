from Calc_module import *

print("Main module: " + __name__)

if __name__=="__main__":
    print("I am from main")

if __name__!="__main__":
    print(add(6,2))
else:
    print(sub(6, 2))