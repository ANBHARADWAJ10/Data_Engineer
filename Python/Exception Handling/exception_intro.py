num = 0
try:
    div = 10 / num
except Exception as e:
    print('Error:', e)
    print('You cannot divide by zero.')
else:
    print('Division successful:', div)
finally:
    print('completed')


