print("Enter the Name of a File to Read: ", end="")
fileName = input()

fileHandle = open(fileName, "r")
content = fileHandle.read()
print("\n----File Contains----")
print(content)