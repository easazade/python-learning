list1 = ["name", 5, True]
print(list1[1])
# we can split lists just like we do it with string
# in python actually a string is like a list of characters. list and string have similar behaviors in python
print(list1)
list1_split = list1[0:2]
print(list1_split)
list1.append(9.3)
print(list1)
# remove function will remove the first matching value. if none will throw an error
list1.remove(9.3)
print(list1)
# we use del keyword for deleting at index
del list1[1]
print(list1)
# popping values
list1.pop(1)
print(list1)
# copying list
list2 = list1.copy()
print(id(list1))
print(id(list2))
# adding values to lists at specific index
list3 = ["ali", "parsa", "mostafa", "milad"]
list3.insert(1, "saeed")
print(list3)
