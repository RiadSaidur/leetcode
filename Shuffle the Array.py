class Solution(object):
  def shuffle(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    shuffle = []

    for i in range(n):
      shuffle.append(nums[i])
      shuffle.append(nums[i+n])
    
    return shuffle