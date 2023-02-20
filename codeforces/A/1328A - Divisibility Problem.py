import math


n = int(input())

for _ in range(n):
  a, b = [ int(x) for x in input().split() ]
  print(math.ceil(a/b)*b-a)