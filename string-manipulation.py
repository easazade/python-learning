name = "alireza easazade"
print(len(name))
name_split = ""
for i in range(name.__len__()):
    name_split += name[i] + "  "
print(name_split)
print("############################")
print("reverse the letters bu negative indexes starting from -1 ")
print("############################")
name_split = ""
for i in range(name.__len__()):
    name_split += name[-i] + " "
print(name_split)
print("mines zero is zero")
print("############################")
print("second letter from end of my name is -> " + name[-2])
print("############################")
print("substring in python")
print("subscting of index 0 to 7 ->" + name[0:7])
print("subscting of index to 7 ->" + name[:7])
print("subscting of index 3 ->" + name[3:])
print("subscting of index undefined ->" + name[:])
print("############################")
print("Formatted Strings : ")
first = "alireza"
last = "easazade"
full = f"{first} {last}"
print(full)
formatted = f"{len(first + last)} {2 + 9} {2.9.__str__()}"
print(formatted)
formatted2 = f"""{"value 1"} 
        {4889}
"""
print(formatted2)
print("############################")
name = "name"
name.upper()  # NAME
name.lower()  # name
name.title()  # first character of each word will be in UpperCase
name = "      name"
print(name.strip())  # removes white spaces from before and end of the string
print(name.lstrip())
print(name.rsplit())
name = "shapoor"
print(name.find("h"))
print(name.replace("sh", "fa"))

name = "alireza easazade"
print("ali" in name)
print("ali" not in name)
