import collections


def removeStones(self, stones):
  def dfs(i, j):
    points.discard((i, j))
    
    for y in rows[i]:
      if (i, y) in points:
        dfs(i, y)

    for x in cols[j]:
      if (x, j) in points:
        dfs(x, j)

  points, island = {(i, j) for i, j in stones}, 0
  rows, cols = collections.defaultdict(list), collections.defaultdict(list)

  for i, j in stones:
    rows[i].append(j)
    cols[j].append(i)

  for i, j in stones:
    if (i, j) in points:
      dfs(i, j)
      island += 1

  return len(stones) - island