nums = []
print("Enter 5 elements for the list: ")
for i in range(5):
    val = int(input())
    nums.append(val)

sum = 0

for i in range(5):
    if nums[i]%2 == 0:
        sum = sum + nums[i]

print("\nSum of Even Numbers is", sum)