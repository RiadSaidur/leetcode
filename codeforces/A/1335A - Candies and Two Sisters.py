n = int(input())

for _ in range(n):
  candies = int(input())
  
  if candies == 2:
    print(0)
  elif candies % 2:
    print(candies//2)
  else:
    print(candies//2 - 1)