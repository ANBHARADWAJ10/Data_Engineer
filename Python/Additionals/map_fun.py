nums = [1, 2, 3, 4, 5]
squares = map(lambda x:x**2, nums)
print(list(squares))

#map =  map(expression, iterable) --> ex: map(lambda x: x**2, iterable) // 
# assigning value --> map(lambda x,y : x + y, iterable,iterable) // place as many iterables as you want.
# Here iterable is nothin but a list.
#enumerate = enumerate(iterable) --> it can be used to bring out of the index as well
#zip = zip(iterable,iterable) --> can iterate two integers side by side

data = [i*2 for i in nums]
print(data)

extra =[None if i < 5 else i for i in data]

print(extra)