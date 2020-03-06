def increment(number: int, by) -> int:
    return number + by


def function_with_multiple_return_values(arg1=5):
    # the return type is a Tuple which is an unmodifiable list
    return "alireza", 20 + arg1


print(increment(5, 2))
name, age = function_with_multiple_return_values()
print(name)
print(age)

# using keyword arguments to make code more readable
increment(7, by=2)


def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(5, 9, 8, 7, 4, 6))


# this is how we create an object in python
def save_user(**user):
    ali = ""
    print(f"user -> {user['id']} - {user['name']} - {user['phone']}")


save_user(id=54, name="alireza", phone="09117158746")
save_user(id=16, name="saman", phone="09116598777")
