print("Enter the Name of a File: ", end="")
fileName = input()
print("Enter the Text to Write in File: ", end="")
text = input()

fileHandle = open(fileName, "w")
fileHandle.write(text)
fileHandle.close()
print("\nThe given content is written on the file successfully!")