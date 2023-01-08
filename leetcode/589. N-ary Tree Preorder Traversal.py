from typing import List


class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children
    

def preorder(root: Node) -> List[int]:
  if not root:
    return []

  nodeStack = [root]
  result = []

  while nodeStack:
    top = nodeStack.pop()
    result.append(top.val)
    nodeStack.extend(reversed(top.children))
  
  return result