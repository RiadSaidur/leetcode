from typing import List


def searchInsert(nums: List[int], target: int) -> int:
  left, right = 0, len(nums)-1

  mid = (left+right)//2

  while left <= right:
    mid = (left+right)//2

    if target == nums[mid]:
      return mid
    elif target < nums[mid]:
      right = mid - 1
    else:
      left = mid + 1

  if not mid:
    return mid+1 if target > nums[mid] else mid

  if right == mid:
    return mid+1 if target > nums[mid] else mid-1
  
  return mid
  


print(searchInsert([1,3,5,6], 8))
