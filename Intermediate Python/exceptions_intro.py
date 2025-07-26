# Errors and Exceptions

# file = open('Outline.txt', 'r')
# reader = file.readlines()
# for line in reader:
#     if line.startswith('Multi'):
#         print(line.strip())

# raise

x = -5
# if x < 0:
#     raise Exception('x should be positive')\

# assert(x>=0), ' x is not positive'

try:
    a = 4 / 0
except ZeroDivisionError as e:
    print(e)
else:
    print("Goodbye")
finally:
    print("Goodbye Goodbye")

# Create our own exceptions by creating an exceptions class
# all we have to do is add error at the end of the class

class ValueTooHighError(Exception):
    pass
class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 10:
        raise ValueTooHighError('value is high')
    elif x < 5:
        raise ValueTooLowError('value is low', x)

print(test_value(1))