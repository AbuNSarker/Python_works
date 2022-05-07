from numpy import *

# Create a matrix
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
# Alternative way to create a matrix
B = matrix('1 2 3; 4 5 6; 7 8 9')

print("A =", A)
print("A[1] =", A[1])          # 2nd row
print("A[1][2] =", A[1][2])    # 3rd element of 2nd row
print("A[0][-1] =", A[0][-1])  # Last element of 1st Row

column = []                    # empty list
for row in A:
    column.append(row[2])
print("3rd column of A=", column)


# Martix Multiplication
C = A*B

print("B =", B)
# print(C)
# print(A.max())
# print(C.min())
