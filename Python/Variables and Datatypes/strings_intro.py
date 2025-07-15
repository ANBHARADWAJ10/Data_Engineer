# string

mystring = 'nikhil'
print(type(mystring))
print(mystring)
print('I\'m nikhil')
print("I'm Nikhil")
print(''' used for multiline string
super man''')

mystring = 'Hello World   '
char = mystring[0]
print(char)
print(mystring[1:3])
new_stirng = mystring.strip()
print(new_stirng)
print(mystring.upper())
print(mystring.lower())
print(mystring.startswith('Hello'))
print(mystring.endswith('World'))
print(mystring.count('i'))
print(mystring.find('o'))
print(mystring.replace('i', 'o'))
mylist = mystring.split()
print(mylist)
new_string = ''.join(mylist)
print(new_string)

# add modulo symbol at the place where you wanna import the string and modulo outside and then the string varaible that represents teh
# original name that you wanna place.
str = 'Tom'
n_str = 'Hey this is my fav character %s' %str
print(n_str)

# we'll place %d for decimal value
num = 10
d_str = 'Hey this is my lucky %d' %num
print(d_str)
# %.2f for float
#{:.2f} and {:.2f}  .format(var, var2)


