# primitive types are immutable
x = 1
print("memory location -> " + id(x).__str__())
y = x
print("memory location -> " + id(y).__str__())
x = x + 5
print("memory location -> " + id(x).__str__())

# mutable types
list_of_names = ["ali", "hasan", "yashar"]
print("memory location of list -> " + id(list_of_names).__str__() + "  list size = " + list_of_names.__len__().__str__())
list_of_names.append("sasan")
print("memory location of list -> " + id(list_of_names).__str__() + "  list size = " + list_of_names.__len__().__str__())
