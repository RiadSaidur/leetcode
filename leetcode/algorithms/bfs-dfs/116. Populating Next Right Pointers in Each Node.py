import collections
from typing import Optional


class Node:
  def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
    self.val = val
    self.left = left
    self.right = right
    self.next = next

class Solution:
  def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
      return None

    queue = collections.deque()
    queue.append(root)

    while queue:
      prevNode = None

      for _ in range(len(queue)):
        node = queue.popleft()

        if node:
          queue.append(node.left)
          queue.append(node.right)

        if prevNode:
          prevNode.next = node
          prevNode = prevNode.next
        else:
          prevNode = node

    return root