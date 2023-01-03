class Solution:
  def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    splitedList = []
    current, n = head, 0

    while current:
      n += 1
      current = current.next

    part, left = n//k, n%k

    current = head
    prev = None

    for _ in range(k):
      splitedList.append(current)

      for _ in range(part):
        if current:
          prev = current
          current = current.next

      if left and current:
        left -= 1
        prev = current
        current = current.next

      if prev:
        prev.next = None
      
    return splitedList