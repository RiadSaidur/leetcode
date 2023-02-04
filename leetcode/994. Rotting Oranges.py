import collections
import itertools
from typing import List


def orangesRotting(grid: List[List[int]]) -> int:
  m, n = len(grid), len(grid[0])
  queue = collections.deque()
  fresh = 0

  for i,j in itertools.product(range(m), range(n)):
    if grid[i][j] == 2: queue.append((i,j))
    if grid[i][j] == 1: fresh += 1

  dirs = [[1,0],[-1,0],[0,1],[0,-1]]
  levels = 0
  
  while queue:
    levels += 1

    for _ in range(len(queue)):
      x, y = queue.popleft()

      for dx, dy in dirs:
        if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy] == 1:
          fresh -= 1
          grid[x+dx][y+dy] = 2
          queue.append((x+dx, y+dy))
                  
  return -1 if fresh != 0 else max(levels-1, 0)

print(orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(orangesRotting(grid = [[0,2]]))