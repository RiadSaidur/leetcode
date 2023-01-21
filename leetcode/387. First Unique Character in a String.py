import collections


def firstUniqChar(s: str) -> int:
  charMap = collections.Counter(s)

  for idx, char in enumerate(s):
    if charMap[char] == 1:
      return idx

  return -1

print(firstUniqChar(s = "leetcode"))
print(firstUniqChar(s = "loveleetcode"))
print(firstUniqChar(s = "aabb"))