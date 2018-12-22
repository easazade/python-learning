tuple1 = ("name", 65, True)
list1 = [1, 3, 6, 5, 8, 9]
# in dictionaries you can use key/value pairs. they are unordered collections like maps
dictionary = {
    "id": "0920e2jk",
    "name": "alirezza",
    "phone": "09117158746"
}
print(dictionary)
# adding values to dictionaries
dictionary["pet"] = "cat"
print(dictionary)
# getting values
print(dictionary.get("pet"))
print(dictionary)
# pop items
print(dictionary.popitem())
print(dictionary)

# looping throw
while dictionary.items().__len__() > 0:
    print(dictionary.popitem().__getitem__(1))


