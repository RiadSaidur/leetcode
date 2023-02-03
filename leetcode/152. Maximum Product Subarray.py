from typing import List


def maxProduct(nums: List[int]) -> int:
  result = max(nums)
  currMax, currMin = 1, 1

  for num in nums:
    if num == 0:
      currMax, currMin = 1, 1
      continue
    
    temp = currMax * num
    currMax = max(num * currMax, num * currMin, num)
    currMin = min(temp, num * currMin, num)

    result = max(result, currMax)

  return result
