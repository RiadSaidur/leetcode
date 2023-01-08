class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for idx1, n1 in enumerate(nums):
      for idx2, n2 in enumerate(nums[idx1+1:]):
        if n1+n2 == target: return [idx1, idx2+idx1+1]

nums = [2,7,11,15]
target = 9

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6

def twoSum(nums, target):
  numSet = {}

  for idx, num in enumerate(nums):
    diff = target - num

    if numSet.get(diff, -1) >= 0:
      return [numSet[diff], idx]
    
    numSet[num] = idx

print(twoSum(nums=nums, target=target))