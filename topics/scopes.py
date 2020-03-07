# variables that are created in while loops and for loops and if statements will be accessible outside of them
for i in range(50):
    value = "reza"
    print(i)

value = "shapoor"

print("#####################################")
print()


# if we want to change global variables from within functions we must call global on them
# if we want to read them however it will be fine
def read_global():
    print(value)


def write_global():
    global value
    value = "hessan"


def cant_change_global():
    value = "farshad"  # just defies nwe variable


read_global()
cant_change_global()
read_global()
write_global()
read_global()

# dir() lists all the functions of the given object
print(value.__dir__())
