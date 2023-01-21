from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

#  NAIVE SOLUTION
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  if not head.next:
    return

  root = head
  nodeNo = 0

  while head:
    nodeNo += 1
    head = head.next


  node = root
  if nodeNo == n:
    root = root.next
  else:
    for _ in range(nodeNo - n -1):
      node = node.next
  
  node.next = node.next.next

  return root

# TWO POINTER SOLUTION
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
  slow, fast = head, head

  for _ in range(n):
    fast = fast.next
  
  if not fast:
    return head.next
  
  while fast.next:
    slow = slow.next
    fast = fast.next
  
  slow.next = slow.next.next

  return head