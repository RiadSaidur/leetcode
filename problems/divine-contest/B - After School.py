n, k = list(map(int, input().split()))

numberOfOccurences = 0

for i in range(1, n+1):
  for j in range(1, n+1):
    temp = 0
    
    if i:
      temp = j//i

    if temp == k:
      numberOfOccurences += 1

  if k > n//i:
    break

print(numberOfOccurences)