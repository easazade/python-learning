class Person:
    name: str

    # overriding __init__ method constructor
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    # overriding __str__ method
    def __str__(self) -> str:
        return f"name:{self.name}"


ali = Person("alireza")
print(ali.get_name())

# adding properties to objects at runtime dynamically.
# It can be done but i guess no in their right mind would do it unless they are Javascript developers.
# just ignoring hints for educational purposes
ali.age = 25  # type: ignore
ali.car = "pride"  # type: ignore


def dump(obj: object) -> None:
    for attr in dir(obj):
        if hasattr(obj, attr):
            print("obj.%s = %s" % (attr, getattr(obj, attr)))


dump(ali)
