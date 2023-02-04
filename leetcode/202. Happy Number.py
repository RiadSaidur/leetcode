def isHappy(n: int) -> bool:
  def getSquareOfDigits(n: int) -> int:
    squareOfDigits = 0

    while n:
      squareOfDigits += (n%10) ** 2
      n = n//10
    
    return squareOfDigits

  visited = set()

  while n not in visited:
    visited.add(n)
    n = getSquareOfDigits(n)

    if n == 1:
      return True

  return False

print(isHappy(19))
print(isHappy(2))
print(isHappy(23))