from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

node10 = ListNode(-5)
node9 = ListNode(-2, node10)
node8 = ListNode(-5, node9)
node7 = ListNode(-9, node8)
node6 = ListNode(6, node7)
node5 = ListNode(19, node6)
node4 = ListNode(-4, node5)
node3 = ListNode(7, node4)
node2 = ListNode(7, node3)
node1 = ListNode(-1, node2)

node10.next = node7

head = node1


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
  nodeDict = {}

  while head:
    if nodeDict.get(head, None):
      return nodeDict[head]
    else:
      nodeDict[head] = True
      head = head.next

  return head

print(detectCycle(head=head))