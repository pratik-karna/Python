
numerator = fact          
sub = n - r               
fact = 1
i = 1
while i<=sub:
  fact = i*fact
  i = i+1
denominator = fact     
perm = numerator/denominator

print("\nPermutation =", perm)