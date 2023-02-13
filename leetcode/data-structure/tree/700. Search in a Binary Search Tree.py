from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    def bst(node):
      if not node:
        return node

      if node.val == val:
        return node

      if val > node.val:
        return bst(node.right)
      else:
        return bst(node.left)

    return bst(root)

root = TreeNode(val=4, 
  left=TreeNode(val=2, 
    left=TreeNode(val=1), 
    right=TreeNode(val=3)
  ), 
  right=TreeNode(7))

print(Solution().searchBST(root=root, val=2))