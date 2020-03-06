tuple1 = ("name", 65, True)
list1 = [1, 3, 6, 5, 8, 9]
# in dictionaries you can use key/value pairs. they are unordered collections like maps
# dictionaries are maps but the difference is that not all keys (and values) must be of same specific type
dictionary = {
    "id": "0920e2jk",
    "name": "alirezza",
    "phone": "09117158746",
    "hobbies": ["watch tv", "video games", "mountain climbing"]
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

# looping throw , THIS IS NOT USED HOWEVER , the point of dictionaries is to access values buy their keys
while dictionary.items().__len__() > 0:
    print(dictionary.popitem().__getitem__(1))

# mixed dictionary
dictionary2 = {
    "name": "shpoor",
    2: "somaye",
    True: "wmoadmo",
    False: "w0k0dw0akd"
}
print(dictionary2)
