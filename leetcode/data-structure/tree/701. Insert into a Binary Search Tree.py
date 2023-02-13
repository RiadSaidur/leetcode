from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
      return TreeNode(val=val)

    def bst(node):
      if val > node.val:
        if node.right:
          bst(node.right)
        else:
          node.right = TreeNode(val=val)
          return 
      else:
        if node.left:
          bst(node.left)
        else:
          node.left = TreeNode(val=val)
    
    bst(root)

    return root

root = TreeNode(val=4,
  left=TreeNode(val=2,
    left=TreeNode(val=1),
    right=TreeNode(3)),
  right=TreeNode(7)
)

print(Solution().insertIntoBST(root=root, val=5))