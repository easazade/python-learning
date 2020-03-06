def increment(number: int, by) -> int:
    return number + by


def function_with_multiple_return_values(arg1=5):
    # the return type is a Tuple which is an unmodifiable list
    return "alireza", 20 + arg1


print(increment(5, 2))
print(function_with_multiple_return_values())

# using keyword arguments to make code more readable
increment(7, by=2)


def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


print(multiply(5, 9, 8, 7, 4, 6))
