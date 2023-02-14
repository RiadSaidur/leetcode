from typing import List


def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  rows = len(image)
  cols = len(image[0])

  curr_color = image[sr][sc]

  def dfs(r: int, c: int) -> None:
    if r < 0 or c < 0 or r >= rows or c >= cols or image[r][c] != curr_color or image[r][c] == color:
      return
    
    image[r][c] = color

    dfs(r+1, c)
    dfs(r-1, c)
    dfs(r, c+1)
    dfs(r, c-1)

  dfs(sr, sc)

  return image