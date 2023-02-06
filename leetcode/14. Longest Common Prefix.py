from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
  str = ''

  for i in range(len(strs[0])):
    for s in strs:
      if i == len(s) or strs[0][i] != s[i]:
        return str
    str += strs[0][i]

  return str

print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ["dog","racecar","car"]))