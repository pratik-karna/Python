print("Enter the Name of First File: ", end="")
fileOne = input()
print("Enter the Name of Second File: ", end="")
fileTwo = input()
print("Enter the Name of Third File: ", end="")
fileThree = input()

content = ""
fh = open(fileOne, "r")
for line in fh:
    content = content + line + '\n'
fh.close()

fh = open(fileTwo, "r")
for line in fh:
    content = content + line + '\n'
fh.close()

fh = open(fileThree, "w")
fh.write(content)

print("\nFile merged successfully!")