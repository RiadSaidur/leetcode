from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
  reverseHead = None

  while(head):
    if(reverseHead):
      temp = head
      head = head.next
      temp.next = reverseHead
      reverseHead = temp
    else:
      reverseHead = head
      head = head.next
      reverseHead.next = None
  
  return reverseHead


reverseHead = reverseList(head=head)

while(reverseHead):
  print(reverseHead.val)
  reverseHead = reverseHead.next