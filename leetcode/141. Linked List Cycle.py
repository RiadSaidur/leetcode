from typing import Optional


class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
  visited = set()

  if not head:
    return False
    
  slow = head
  fast = head.next

  while fast and fast.next:
    if fast in visited:
      return True
    visited.add(slow)
    slow = slow.next
    fast = fast.next.next
  
  return False