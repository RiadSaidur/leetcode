import heapq
from typing import List


def lastStoneWeight(stones: List[int]) -> int:
  for idx, stone in enumerate(stones):
    stones[idx] = -stone
    
  heapq.heapify(stones)
  
  while stones:
    s1 = -heapq.heappop(stones)
    if not stones:
      return s1
    s2 = -heapq.heappop(stones)
    heapq.heappush(stones, s2 - s1)
  
  return 0

print(lastStoneWeight([2,7,4,1,8,1]))
print(lastStoneWeight([1]))