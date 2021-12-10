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