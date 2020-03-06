class Person:
    name: str

    # overriding __init__ method constructor
    def __init__(self, name): self.name = name

    def get_name(self) -> str: return self.name

    # overriding __str__ method
    def __str__(self): return f"name:{self.name}"


ali = Person("alireza")
print(ali.get_name())

# adding properties to objects at runtime dynamically
ali.age = 25
ali.car = "pride"


def dump(obj):
    for attr in dir(obj):
        if hasattr(obj, attr):
            print("obj.%s = %s" % (attr, getattr(obj, attr)))


dump(ali)
