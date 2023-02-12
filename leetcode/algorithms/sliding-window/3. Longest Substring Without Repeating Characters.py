def lengthOfLongestSubstring(s: str) -> int:
  subSet = set()
  
  left, maxLength = 0, 0

  for char in s:
    while char in subSet:
      subSet.remove(s[left])
      left += 1
    
    subSet.add(char)
    maxLength = max(maxLength, len(subSet))

  return maxLength



print(lengthOfLongestSubstring(s = "abcabcbb"))