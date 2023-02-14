import collections
from typing import Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
  node = root

  while node:
    if node.val < p.val and node.val < q.val:
      node = node.right
    elif node.val > p.val and node.val > q.val:
      node = node.left
    else:
      return node