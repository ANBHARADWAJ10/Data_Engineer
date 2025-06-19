def greet(name):
    print(f"Hello, {name}!")



name = "Nikhil"
greet(name)


def add_num(num1: int, num2: int) -> int:

    num3 = num1 + num2
    return num3


num1 = 10
num2 = 20

result = add_num(num1, num2)
print(result)
import math
# Function to check if a number is even or odd

# if a number is a prime number or not
def is_prime(num: int) -> int:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False # excluding the even numbers greater than 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

# string made of first middle and last characters

name = "Nikhil"
def f_m_l(name: str) -> str:
    if len(name) < 3:
        return name
    first = name[0]
    second = name[len(name) // 2]
    last = name[-1]
    return first + second + last

print(f_m_l(name))
