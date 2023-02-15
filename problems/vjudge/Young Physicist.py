n = int(input())

x, y, z = 0, 0, 0

for _ in range(n):
  v = list(map(int, input().split()))
  x += v[0]
  y += v[1]
  z += v[2]

if x == y == z == 0:
  print('YES')
else:
  print('NO')