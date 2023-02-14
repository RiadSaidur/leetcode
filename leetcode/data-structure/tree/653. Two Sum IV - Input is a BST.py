from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
    
class Solution:
  def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    nodeSet = set()

    def bst(node):
      if not node:
        return False

      if k - node.val in nodeSet:
        return True

      nodeSet.add(node.val)

      return bst(node.left) or bst(node.right)
      
    return bst(root)
      
# root = TreeNode(5, 
#   TreeNode(3, 
#       TreeNode(2), TreeNode(4)
#     ), 
#     TreeNode(6, 
#       None, 
#       TreeNode(7)
#     )
#   )

root = TreeNode(1)

print(Solution().findTarget(root=root, k=2))