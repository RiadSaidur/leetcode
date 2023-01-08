from typing import List

nums = [-1,0,3,5,9,12]

target1 = 9
target2 = 1

def search(nums: List[int], target: int) -> int:
  left = 0
  right = len(nums) - 1

  while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
      return mid
    elif nums[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
    
  return -1

print(search(nums=nums, target=target1))
print(search(nums=nums, target=target2))