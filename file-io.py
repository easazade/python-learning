file = open("files//info.txt", 'r')
print(type(file))
content = file.read()
print(content)
file.readline()
# result will be [] because we have already read all of the file
# and the pointer has reached end of file

# reading line by line
# first we must put the pointer to the first character
file.seek(0)
content = file.readline()
while content:
    print(content)  # each line has a\n at end of it it will be printed as well
    content = file.readline()

# read all lines
file.seek(0)
list_of_lines = file.readlines()
print(list_of_lines)
# removing \n from each line stored in our listOfLines
lines_without_return = [i.rstrip("\n") for i in list_of_lines]
print(lines_without_return)

# if we have opened our file in write mode we must call close() on it to commit changes
# other wise there will be no changes to the file

