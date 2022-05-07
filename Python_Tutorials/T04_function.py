# Create a function that returns a single value
def add(x, y):
    p = x+y
    return p

out = add(2, 3)
print(out)

# Create a function that returns multiple values
def add_sub(x, y):
    p = x+y
    q = x-y
    return p, q

out1, out2 = add_sub(2, 3)
print(out1, out2)

# Lambda function
x = 5
f = lambda x: x*x
print('SQRT =',f(5))

# Memory Address of a variable
g= lambda x: print('Memory Address:', id(x))

a = 5
print('Memory Address:', id(a))
g(a)

