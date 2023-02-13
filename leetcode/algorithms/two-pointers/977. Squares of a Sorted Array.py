import heapq
from typing import List


def sortedSquares(nums: List[int]) -> List[int]:
  nums.sort(key=lambda x: abs(x))
  return [x**2 for x in nums]
  

print(sortedSquares(nums = [-4,-1,0,3,10]))