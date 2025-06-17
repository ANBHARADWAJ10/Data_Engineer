# Dictionary is a collection of key-value pairs.
# Dictionaries are unordered collections of items.

# method 1 to creating a dictionary
my_dict = {
    "Name": "Nikhil Bharadwaj",
    "Age": 23,
    "Height": 5.7
}

print(my_dict)

# method 2 to creating a dictionary

my_dic2 = dict(name="Nikhil Bharadwaj", age=23, height=5.7)

# Accessing values in a dictionary

value01 = my_dict["Name"]
print(value01)

print(my_dict.get("Age"))

print(my_dict.get("email", "Not Found"))  # returns "Not Found" if key doesn't exist

# Modifying values in a dictionary

my_dict["Age"] = 24
print(my_dict)

# Adding new key-value pairs to a dictionary
my_dict["email"] = "abcd@gmail.com"
print(my_dict)

# Removing key-value pairs from a dictionary
my_dict.pop("Height") # removes the key "Height" and its value
my_dict.popitem()  # removes the last inserted key-value pair
del my_dic2["age"] # removes the key "age" and its value
my_dic2.clear()  # removes all key-value pairs from the dictionary
print(my_dict)
print(my_dic2)

# Iterating through a dictionary and printing keys
print("Keys in my_dict:")
for key in my_dict:
    print("Keys:", key)

# Iterating through a dictionary and printing values
print("Values in my_dict:")
for value in my_dict:
    print("values:",my_dict[value])

# Iterating through a dictionary and printing key-value pairs

for key, value in my_dict.items():
    print(f"{key}: {value}")

# Useful Dictionary Methods

# | Method      | Description                          | Example                    |
# | ----------- | ------------------------------------ | -------------------------- |
# | `get()`     | Get value for key                    | `dict.get("key", default)` |
# | `keys()`    | Returns list of keys                 | `dict.keys()`              |
# | `values()`  | Returns list of values               | `dict.values()`            |
# | `items()`   | Returns list of key-value pairs      | `dict.items()`             |
# | `update()`  | Merge another dictionary             | `dict.update(other_dict)`  |
# | `pop(key)`  | Remove and return item with key      | `dict.pop("key")`          |
# | `popitem()` | Remove and return last inserted item | `dict.popitem()`           |
# | `clear()`   | Remove all items                     | `dict.clear()`             |
# | ----------- | ------------------------------------ | -------------------------- |
