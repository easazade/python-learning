# if statement
age = 4
if age >= 10:
    print("he is big boy")
    print("he is, isn't he")
elif age <= 5:
    print("he is a baby")
    print("he is a baby")
    print("he is a baby")
else:
    print("he is alright")

# for loop
# everything that is iterable in python can be looped over like strings
value = ""
for x in "Python":
    value += f"{x} "
print(value)

numbers = [1, 6, 9, 7, 2, 5, 1]
value = ""
for num in numbers:
    value += f"{num} "
print(value)

value = ""
for i in range(10):  # range objects consume vey low memory even if we create range(5000000)
    value += f"{i} "
print(value)

for num in numbers:
    if num == 7:
        print("num 7 found")
        break
else:  # this else clause is executed against our for clause and runs if for break is not called
    print("there is no num 7 in list")

# there is only another type of loops in python which are while loops
answer = 75
guess = 0
while guess != answer:
    entry = input("guess the number : ")
    if not type("").isnumeric(entry):
        entry = input("please right a number")
    else:
        guess = int(entry)
