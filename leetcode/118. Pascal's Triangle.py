from typing import List


def generate(numRows: int) -> List[List[int]]:
  result = [[1]]

  for i in range(numRows-1):
    result.append([])
    result[i+1].append(1)
    for j in range(len(result[i])-1):
      result[i+1].append(result[i][j] + result[i][j+1])
    
    result[i+1].append(1)

  return result


print(generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])
# print(generate(1))