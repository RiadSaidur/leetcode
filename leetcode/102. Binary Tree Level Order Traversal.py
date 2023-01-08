import collections
from typing import List, Optional

"""
# root = [1,2,3,4,null,null,5]
# Expected = [[1],[2,3],[4,5]]
"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
  if root is None:
    return []

  result = []

  queue = collections.deque()
  queue.append(root)

  while queue:
    level = []
    for _ in range(len(queue)):
      node = queue.popleft()
      if node:
        level.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    if level:
      result.append(level)
  
  return result

