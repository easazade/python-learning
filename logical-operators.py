name = "alireza"
if not name:
    print("name is empty")
else:
    print(f"name is {name}")

age = 35
if 18 <= age < 65:  # this is called chaining comparison operators
    print("you can ride with us")

my_age = 45
if 18 <= age < 65 > my_age:  # this is called chaining comparison operators
    print("both of you can ride with us")
