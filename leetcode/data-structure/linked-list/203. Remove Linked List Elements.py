from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
  if not head:
    return head

  prev = ListNode()
  root = prev

  while head:
    if head.val != val:
      prev.next = head
      prev = prev.next
    head = head.next
  
  prev.next = None
  
  return root.next