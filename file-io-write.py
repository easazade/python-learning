# if we have opened our file in write mode we must call close() on it to commit changes
# other wise there will be no changes to the file
file = open("files//file.txt", 'w')
# 'w' mode is always create an empty file then write to
# if file already exists it will replace it with a new empty file so BE CAREFUL
# if you want to open an existing file and append to it and also read from it use 'a+' mode
lines = ["this is the first line", "this is the second line", "and this is the third line"]
for line in lines:
    file.write(f"{line}\n")
file.close()

# to append lines to the existing files we must open the file in append mode 'a'
# append mode will also create a new file if not already exists
# 'a+' mode is also allows you to read beside writing to existing file
file = open("files//file.txt", 'a')
for i in range(10):
    file.write(f"appending new line {i}\n")
file.close()

# besides 3 modes of 'r' , 'w' , 'a' there are 3 other modes of 'r+' , 'w+' , 'a+'

# with statement is used with files and what it does is that it will close the file for us automatically
with open("files//file2.txt", 'a+') as file:
    file.write("here is one more line\n")
    file.seek(0)
    content = file.read()
    print(content)
    # no file.close() method with takes care of that for us

