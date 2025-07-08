import string

a = 24
b = str(a)
print(type(b))

num1 = 24
num2 = 32
num1, num2 = num2, num1
print(num1, num2)

name = 'Nikhil Bharadwaj'
count = 0
for i in name:
    if i in ['a','e','i','o','u'] or i in ['A','E','I','O','U']:
        count += 1
print(count)

reverse_string = ''.join(reversed(name))

slicing = name[::-1]
print(slicing)
if slicing in name:
    print(True)
else:
    print(False)

n = 24
n2 = 56
n3 = 12
largest = max(n, n2, n3)
print(largest)
import math
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True


