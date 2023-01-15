# 1A3B
secret = "1807"
guess  = "7810"

secret = "1123"
guess  = "0111"

# secret = "11"
# guess = "10"

# secret = "11"
# guess = "01"

# secret = "011"
# guess = "110"

# secret = "1122"
# guess = "1222"

# secret = "1122"
# guess = "0001"

def getHint(secret: str, guess: str) -> str:
  bulls, cows = 0, 0

  secretsMap = {}
  guessesMap = {}

  for i in range(len(secret)):
    if secretsMap.get(secret[i]):
      secretsMap[secret[i]].add(i)
    else:
      secretsMap[secret[i]] = { i }

    if guessesMap.get(guess[i]):
      guessesMap[guess[i]].add(i)
    else:
      guessesMap[guess[i]] = { i }

  for char in set(secret):
    if guessesMap.get(char):
      commons = len(secretsMap[char].intersection(guessesMap[char]))
      bulls += commons
      cows += min(len(secretsMap[char]), len(guessesMap[char])) - commons
  
  return f'{bulls}A{cows}B'


print(getHint(secret=secret, guess=guess))