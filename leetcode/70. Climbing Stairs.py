def climbStairs(n: int) -> int:
  if n == 0:
    return 0
  elif n== 1:
    return 1
  
  prev = 0
  curr = 1

  for _ in range(n-1):
    prev, curr = curr, curr + prev

  return curr + prev

print(climbStairs(3))
print(climbStairs(2))
print(climbStairs(4))