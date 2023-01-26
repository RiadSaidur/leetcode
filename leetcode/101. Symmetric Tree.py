from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root: return True
    
    def dfs(left, right):
      if not left and not right: return True
      if not left or not right: return False

      if left.val == right.val:
        return dfs(left.left, right.right) and dfs(left.right, right.left)
      return False

    return dfs(root.left, root.right)