mylist = list()
print("Enter 5 elements for the tuple: ")
for i in range(5):
    mylist.append(input())

mytuple = tuple(mylist)

revtuple = mytuple[::-1]

print("\nOriginal Tuple:", mytuple)
print("Reversed Tuple:", revtuple)