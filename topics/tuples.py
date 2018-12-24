
# unmodifiable lists that are much less used than lists
tuple1 = (9, 9, "name", True)
print(tuple1.__len__())
# count() returns occurrences of element in a tuple
print(tuple1.count(9))
# index() returns smallest index of element in tuple
print(tuple1.index(True))
