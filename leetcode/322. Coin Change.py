import collections
from typing import List


class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    q = collections.deque()
    q.append((amount, 0))
    
    visited = set()
    visited.add(amount)
    
    while q:
      curr_amt, level = q.popleft()

      if curr_amt == 0:
        return level

      for c in coins:
        new_amt = curr_amt - c

        if new_amt >= 0 and new_amt not in visited:
          q.append((new_amt, level+1))
          visited.add(new_amt)
          
    return -1