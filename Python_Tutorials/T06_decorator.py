# Decorator... or Functional Programming

def division(x,y):
    print (x/y)

def change_order(dfun):
    def inner_fun(x,y):
        if x<y:
            x,y = y,x
        return dfun(x,y)
    return inner_fun

division = change_order(division)

division(2,10)