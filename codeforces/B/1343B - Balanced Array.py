n = int(input())

for _ in range(n):
  num = int(input())
  
  if num % 2 or num == 2:
    print('NO')
  else:
    arr = []
    evenSum, oddSum = 0, 0

    for i in range(2, num+1, 2):
      evenSum += i
      arr.append(i)

    for i in range(1, num-1, 2):
      oddSum += i
      arr.append(i)
    if (evenSum-oddSum) % 2:
      arr.append(evenSum-oddSum)
      print('YES')
      print(*arr, sep=' ')
    else:
      print('NO')

