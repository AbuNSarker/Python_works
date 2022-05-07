import numpy as np;

# Creating 1D array
arr1 = np.array([2, 3, 4, 5, 6, 7]);
arr2 = arr1.copy();

print(arr1);
print(arr2);
# print(id(arr1));
# print(id(arr2));

# Create 2-dimensional array
arr3 = np.array([
    [1, 2, 3, 4, 5, 6],
    [4, 5, 6, 7, 8, 9]
]);
print(arr3);

# N-dimensional array to single-dimensional array
arr4 = arr3.flatten();
print(arr4);

# single-dimensional array to 2- and 3-dimensional array
arr5 = arr4.reshape(3, 4)
arr6 = arr4.reshape(2, 3, 2)
print(arr5);
print(arr6);
