# Find the Factorial using Recursion Approach 

n = int(input("Enter the value of n,  n = "))

def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

fact = factorial(n)
print(f'Factorial of {n} is {n}! = {fact}')