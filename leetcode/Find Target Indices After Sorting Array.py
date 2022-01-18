class Solution(object):
  def targetIndices(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums.sort()

    return list(i for i, num in enumerate(nums) if num == target)