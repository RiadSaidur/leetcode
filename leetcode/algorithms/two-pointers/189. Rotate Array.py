from typing import List


class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(ar: List[int], left, right) -> None:
      while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left+1, right-1

    k = k % len(nums)
    
    left, right = 0, len(nums)-1
    reverse(nums, left, right)

    left, right = 0, k-1
    reverse(nums, left, right)

    left, right = k, len(nums)-1
    reverse(nums, left, right)



# nums = [-1,-100,3,99]
# k = 2

nums = [1,2,3,4,5,6,7]
k = 3

# nums = [1]
# k = 1

Solution().rotate(nums=nums, k=k)

print(nums)
