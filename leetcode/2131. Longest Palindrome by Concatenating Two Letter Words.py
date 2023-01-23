from collections import Counter
from typing import List


def longestPalindrome(words: List[str]) -> int:
  n = 0

  seen = {}
  pairedWords = {}

  # ei loop e ami "gg" emn paired thakle paired e dhukaaitesi
  # new word paile oita seen e dhukiatesi "ty" emn
  # seen e jodi ulta tah pai "yt" er mtw tyla oitar count komay ditesi r n++
  for word in words:
    if len(set(word)) == 1:
      pairedWords[word] = pairedWords.get(word, 0) + 1
    elif seen.get(word[::-1], 0):
      seen[word[::-1]] -= 1
      n += 2
    else:
      seen[word] = seen.get(word, 0) + 1

  # then eikhane paired gula jodi even hoy tyla oitar purta nitasi "gg" "gg" emn gula
  # r count jodi odd hoy tyla -1 ta nitasi
  for count in pairedWords.values():
    if not count % 2:
      n += count
    else:
      if not n % 2:
        n += count
      else:
        n += count - 1
    
  return n*2

# def longestPalindrome(words: List[str]) -> int:
#   wordCount = Counter(words)

#   for word in wordCount:
#     if wordCount[word]

# print(longestPalindrome(words = ["lc","cl","gg"]))
# print(longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
# print(longestPalindrome(words = ["cc","ll","xx"]))
# print(longestPalindrome(words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))
# print(longestPalindrome(["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"]))
# print(longestPalindrome(["bb","bb"]))
print(longestPalindrome(["zb","bb","zy","bz","yb","yz","zz","zy","zb","zz","by","by","bb","bz","bz","yy","bz","zz","bz","yy","yz","yz","zz","zy","by","zy","bb","yz","yy","by","zy","yz","yy","by","zz","bb","yb","by","yy","zb","bb","yz","yb","zz","by","yb","zy","bb","yz","zb","zy","yy","bb","by","yb","yb","bb","bb"]))