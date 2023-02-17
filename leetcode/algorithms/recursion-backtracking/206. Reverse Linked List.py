from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
    
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    reverseHead = None

    while head:
      if reverseHead:
        temp = head
        head = head.next
        temp.next = reverseHead
        reverseHead = temp
      else:
        reverseHead = head
        head = head.next
        reverseHead.next = None

    return reverseHead
    