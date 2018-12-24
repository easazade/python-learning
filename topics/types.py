# python is dynamic types
from datetime import time

name = 95
print(type(name))
name = "alireza"
print(type(name))
name = 9.3
print(type(name))
name = True
print(type(name))
name = time()
print(type(name))
name = type("some string")
print(type(name))

# type annotations which will be noticed by mypy linter note that python has different linters
# mypy is not installed right now
age: int = 19
age = "dpawmdp"
