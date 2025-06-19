class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

d1 = Dog("Buddy", 5)
d2 = Dog("Max", 3)

print("d1:", d1.name,d1.age)
print('d2:', d2.name, d2.age)

print(d1)