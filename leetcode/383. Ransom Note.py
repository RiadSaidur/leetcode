import collections


def canConstruct(ransomNote: str, magazine: str) -> bool:
  magazineMap = collections.Counter(magazine)

  for char in ransomNote:
    if not magazineMap.get(char, 0):
      return False

    magazineMap[char] -= 1
  
  return True

print(canConstruct(ransomNote = "a", magazine = "b"))
print(canConstruct(ransomNote = "aa", magazine = "ab"))
print(canConstruct(ransomNote = "aa", magazine = "aab"))