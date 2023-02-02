import collections
from typing import List, Optional


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    queue = collections.deque([root])
    result = []

    while queue:
      right = None
      for _ in range(len(queue)):
        node = queue.popleft()
        if node:
          right = node
          queue.append(node.left)
          queue.append(node.right)
      if right:
        result.append(right.val)
    
    return result
