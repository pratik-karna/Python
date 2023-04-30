number = int(input("Enter number: "))

flag = 1

for i in range(2, int(number / 2)):
    if number % i == 0:
        flag = 0
        break

if flag == 1 and number >= 2:
    print("PRIME")
else:
    print("NOT PRIME")
