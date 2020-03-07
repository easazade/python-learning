# python is dynamic types
from datetime import time

obj = 95
print(type(obj))
obj = "alireza"
print(type(obj))
obj = 9.3
print(type(obj))
obj = True
print(type(obj))
obj = time()
print(type(obj))
obj = type("some string")
print(type(obj))

# type annotations which will be noticed by mypy linter note that python has different linters
# mypy is not installed right now
age: int = 19
age = "dpawmdp"
