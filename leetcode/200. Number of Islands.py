from typing import List

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

# grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

def numIslands(grid: List[List[str]]) -> int:
  islands = 0

  row = len(grid)
  column = len(grid[0])

  def fill(r, c):
    if r < 0 or c < 0 or r >= row or c >= column or grid[r][c] == '0':
      return
    
    grid[r][c] = '0'

    fill(r+1, c)
    fill(r-1, c)
    fill(r, c+1)
    fill(r, c-1)

  for i in range(row):
    for j in range(column):
      if grid[i][j] == '1':
        islands += 1
        fill(i, j)


  return islands

print(numIslands(grid))