water = int(input())
x = sum(list(map(int, str(water))))
total = water

for i in range(6):
  water += x
  total += water

print(total)