def isBadVersion(version: int) -> bool:
  pass

def firstBadVersion(self, n: int) -> int:
  left, right = 1, n

  bad = -1

  while left <= right:
    mid = (left+right)//2

    if isBadVersion(mid):
      bad = mid
      right = mid - 1
    else:
      left = mid + 1

  return bad