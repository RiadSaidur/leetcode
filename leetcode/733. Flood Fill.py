from typing import List


image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2

# image = [[0,0,0],[0,0,0]]
# sr = 0
# sc = 0
# color = 0

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  row = len(image)
  column = len(image[0])

  curr_color = image[sr][sc]

  def dfs(r, c):
    if r < 0 or c < 0 or r >= row or c >= column or image[r][c] != curr_color or image[r][c] == color:
      return

    image[r][c] = color

    dfs(r+1, c)
    dfs(r, c+1)
    dfs(r-1, c)
    dfs(r, c-1)
  
  dfs(r=sr, c=sc)

  return image

print(floodFill(image=image, sr=sr, sc=sc, color=color))