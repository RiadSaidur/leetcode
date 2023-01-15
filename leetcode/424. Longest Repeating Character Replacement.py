def characterReplacement(s: str, k: int) -> int:
  charMap = {}
  result  = 0
  length = 0
  maxFrequency = 0

  for idx, char in enumerate(s):
    charMap[char] = charMap.get(char, 0) + 1
    maxFrequency = max(maxFrequency, charMap[char])

    if idx+1 - length - maxFrequency > k:
      charMap[s[length]] -= 1
      length += 1

    result = max(result, idx - length + 1)
  return result

# print(characterReplacement('ABAB', 2))
print(characterReplacement('AABABBA', 1))