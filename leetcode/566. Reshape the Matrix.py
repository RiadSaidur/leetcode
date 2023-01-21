from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
  if r*c != len(mat) * len(mat[0]) or r == len(mat):
    return mat
  
  top = 0
  left = 0

  result = []

  for i in range(r):
    result.append([])
    for j in range(c):
      result[i].append(mat[top][left])
      left += 1
      if left >= len(mat[0]):
        left = 0
        top += 1
  
  return result

# print(matrixReshape([[1,2],[3,4]], r = 1, c = 4))
# print(matrixReshape([[1,2],[3,4]], r = 2, c = 4))
# print(matrixReshape([[1,2,3,4],[5,6,7,8]], r = 4, c = 2))