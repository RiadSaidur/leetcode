from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    result = []

    def dfs(root):
      if not root: return
      dfs(root.left)
      result.append(root.val)
      dfs(root.right)

    dfs(root)

    if not result: return -1
    return result[k-1]

print(Solution().kthSmallest(root, 3))