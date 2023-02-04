from typing import List


def findBall(grid: List[List[int]]) -> List[int]:
  rows = len(grid)
  cols = len(grid[0])

  def drop(i,j):
    if i == rows: return j
    if j == cols-1 and grid[i][j] == 1: return -1
    if j == 0 and grid[i][j] == -1: return -1
    if grid[i][j] == 1 and grid[i][j+1] == -1: return -1
    if grid[i][j] == -1 and grid[i][j-1] == 1: return -1

    return drop(i+1,j+grid[i][j])
  
  return [drop(0,j) for j in range(cols)]


  

print(findBall(grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
print(findBall(grid = [[-1]]))