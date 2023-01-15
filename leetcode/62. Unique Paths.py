m = 1
n = 1


def uniquePaths(m: int, n: int) -> int:
  if m == 1 and n == 1:
    return 1
    
  row = [1] * n

  row[0] = 0

  for _ in range(m-1):
    newRow = [1]
    for j in range(1, n):
      newRow.append(row[j] + newRow[j-1])
    row = newRow
  
  return row[n-1]
    

print(uniquePaths(m,n))