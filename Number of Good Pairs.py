class Solution(object):
  def numIdenticalPairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return len(list(pair for pair in combinations(nums, 2) if pair[0] == pair[1]))