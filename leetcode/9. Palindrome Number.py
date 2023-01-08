x1 = 121
x2 = -121
x3 = 10
x4 = 1001

def isPalindrome(x: int) -> bool:
  if x < 0:
    return False
  
  x = str(x)

  for i in range(len(x)//2):
    if x[i] != x[-i-1]:
      return False

  return True

print(isPalindrome(x1))
print(isPalindrome(x2))
print(isPalindrome(x3))
print(isPalindrome(x4))