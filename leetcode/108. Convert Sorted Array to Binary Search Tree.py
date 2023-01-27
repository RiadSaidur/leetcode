from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    def bst(nums):
      if not nums:
        return 

      mid = len(nums)//2

      return TreeNode(nums[mid], bst(nums[:mid]), bst(nums[mid+1:]))

    return bst(nums)