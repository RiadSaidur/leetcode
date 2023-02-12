import collections


def checkInclusion(s1: str, s2: str) -> bool:
  left, width = 0, len(s1)
  
  s1Counter = collections.Counter(s1)
  s2Counter = collections.Counter(s2[:width])

  for i in range(width, len(s2)):
    if s1Counter == s2Counter:
      return True

    s2Counter[s2[left]] -= 1

    if s2Counter[s2[left]] < 1:
      del s2Counter[s2[left]]

    left += 1
      
    s2Counter[s2[i]] = s2Counter.get(s2[i], 0) + 1

  return s1Counter == s2Counter


print(checkInclusion(s1 = "ab", s2 = "eidbaooo"))
print(checkInclusion(s1 = "ab", s2 = "eidboaoo"))
print(checkInclusion(s1 = "adc", s2 = "dcda"))
print(checkInclusion(s1 = "adc", s2 = "wadc"))