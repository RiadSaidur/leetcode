def isIsomorphic(s: str, t: str) -> bool:
  if len(set(s)) != len(set(t)):
    return False

  isoDict = {}

  for char in range(len(t)):
    if t[char] not in isoDict:
      isoDict[t[char]] = s[char]
    elif isoDict[t[char]] != s[char]:
      return False
      
  return True


# BEST SOLUTION
# zipped_set = set(zip(s, t))
# return len(zipped_set) == len(set(s)) == len(set(t))

print(isIsomorphic('egg', 'add'))
print(isIsomorphic('foo', 'bar'))
print(isIsomorphic('paper', 'title'))
print(isIsomorphic('badc', 'baba'))