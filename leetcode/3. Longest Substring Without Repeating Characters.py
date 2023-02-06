def lengthOfLongestSubstring(s: str) -> int:
  subset = set()
  result = 0
  left = 0

  for char in s:
    while char in subset:
      subset.remove(s[left])
      left +=  1
    subset.add(char)
    result = max(result, len(subset))
  
  return result

print(lengthOfLongestSubstring('pwwkew'))