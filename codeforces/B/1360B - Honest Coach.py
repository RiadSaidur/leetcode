for _ in range(int(input())):
  n = int(input())
  athletes = [int(x) for x in input().split()]

  athletes.sort()

  minDiff = float('inf')

  for i in range(n-1, -1, -1):
    minDiff = min(minDiff, abs(athletes[i] - athletes[i-1]))

  print(minDiff)