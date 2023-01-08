def isBadVersion(version: int) -> bool:
  pass

n = 5

def firstBadVersion(n: int) -> int:
  left = 0
  right = n - 1

  bad = -1

  while left <= right:
    mid = (left + right) // 2
    if isBadVersion(mid):
      bad = mid
      right -= 1
    else:
      left = mid + 1
  
  return bad

# print(firstBadVersion(n))