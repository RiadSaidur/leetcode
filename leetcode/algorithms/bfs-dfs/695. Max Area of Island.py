from typing import List


def maxAreaOfIsland(grid: List[List[int]]) -> int:
  rows, columns = len(grid), len(grid[0])
  visited = set()
  maxArea = 0

  def dfs(r, c):
    if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] == 0 or (r,c) in visited:
      return 0

    visited.add((r, c))
    
    return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

  for r in range(rows):
    for c in range(columns):
      maxArea = max(maxArea, dfs(r, c))

  return maxArea