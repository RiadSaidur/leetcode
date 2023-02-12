from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0
    right = 0

    while right < len(nums) and left < len(nums):
      if nums[right] == 0 and nums[left] != 0:
        nums[right], nums[left] = nums[left], nums[right]

      if nums[right] != 0:
        right += 1

      left += 1

    return nums

# print(moveZeroes(nums = [0,1,0,3,12]))
print(moveZeroes([0]))