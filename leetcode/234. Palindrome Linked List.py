from logging.config import _OptionalDictConfigArgs


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def isPalindrome(self, head: _OptionalDictConfigArgs[ListNode]) -> bool:
  slow = head
  fast = head

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  
  prev = None
  while slow:
    temp = slow.next
    slow.next = prev
    prev = slow
    slow = temp

  while prev:
    if head.val != prev.val:
      return False
    head = head.next
    prev = prev.next
  
  return True