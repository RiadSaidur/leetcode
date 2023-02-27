def fairDivision():
  n = int(input())
  candies = [ int(x) for x in input().split() ]

  if n == 1:
    return 'NO'
  
  candies.sort()

  alice, bob = 0, 0
  
  for candy in candies[::-1]:
    if alice > bob:
      bob += candy
    else:
      alice += candy

  if not alice - bob: return 'YES' 
  else: return 'NO'



if __name__ == '__main__':
  for _ in range(int(input())):
    print(fairDivision())