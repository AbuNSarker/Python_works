# Find the odd numbers
arr = [2, 3, 6 , 7, 8, 9 ];

def is_odd(n):
    return n%2==1

odd = list(filter(is_odd,arr));
# OR
odd = list(filter(lambda n:n%2==1,arr));
print('Odd numbers are:', odd);