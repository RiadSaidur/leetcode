from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
  left, right = 0, len(numbers)-1

  while left < right:
    currSum = numbers[left] + numbers[right]
    
    if target == currSum:
      return [left+1, right+1]
    elif target > currSum:
      left += 1
    elif target < currSum:
      right -= 1

print(twoSum(numbers = [2,7,11,15], target = 9))