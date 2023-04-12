nums = []
totEven = 0
totOdd = 0

print("Enter 10 Numbers: ")
for i in range(10):
  nums.insert(i, int(input()))

for i in range(10):
  if nums[i]%2==0:
    totEven = totEven+1
  else:
    totOdd = totOdd+1

print("\nEven Number: ")
print(totEven)
print("Odd Number: ")
print(totOdd)