from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head1 = node1

node11 = ListNode(6)
node10 = ListNode(5, node11)
node9 = ListNode(4, node10)
node8 = ListNode(3, node9)
node7 = ListNode(2, node8)
node6 = ListNode(1, node7)

head2 = node6

def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
  point1, point2 = head, head

  while point1:
    point1 = point1.next

    if point1:
      point1 = point1.next
    else:
      break;
      
    point2 = point2.next
  
  return point2

mid = middleNode(head=head1)
# mid = middleNode(head=head2)

while(mid):
  print(mid.val)
  mid = mid.next