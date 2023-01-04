from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

# node1 = ListNode(1)

node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)

# node4 = ListNode(2)

list1 = node1
list2 = node4

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  if not list1:
    return list2
  elif not list2:
    return list1

  cur1 = list1
  cur2 = list2

  temp = None
  
  if cur1.val >= cur2.val:
    temp = cur2
    cur2 = cur2.next
  else:
    temp = cur1
    cur1 = cur1.next
    
  tempHead = temp

  while(cur1):
    while(cur2 and cur1.val >= cur2.val):
      if temp:
        temp.next = cur2
      else:
        temp = cur2
        tempHead = temp
      cur2 = cur2.next
      temp = temp.next
      temp.next = None
    temp.next = cur1
    cur1 = cur1.next
    temp = temp.next
  else:
    if cur2:
      temp.next = cur2

  return tempHead

  

merged = mergeTwoLists(list1=list1, list2=list2)
# merged = mergeTwoLists(ListNode(), ListNode())

while(merged):
  print(merged.val)
  merged = merged.next