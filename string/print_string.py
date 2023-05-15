print("How many string to enter ? ", end="")
noOfString = int(input())

print("Enter", noOfString, "Strings followed by ENTER key: ", end="")
mylist = list()
for i in range(noOfString):
    mystring = input()
    mylist.append(mystring)

print("\nStrings entered by you are:")
for i in range(noOfString):
    print("String No.", i+1, ": \"", mylist[i], "\"", sep="")
    
