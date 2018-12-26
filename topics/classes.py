class Person:
    name: str

    def __init__(self, name): self.name = name  # overriding __init__ methods constructor

    def get_name(self) -> str: return self.name

    def __str__(self): return f"name:{self.name}"  # overriding __str__ methods


ali = Person("alireza")
print(ali.get_name())

# adding properties to objects at runtime dynamically
ali.age = 25
ali.car = "pride"

# build-in __str__ methods
print(ali.__str__())

l = object