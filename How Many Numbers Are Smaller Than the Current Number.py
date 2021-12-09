class Solution(object):
  def smallerNumbersThanCurrent(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    return list(sorted(nums).index(num) for num in nums)