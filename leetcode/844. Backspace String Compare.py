def backspaceCompare(s: str, t: str) -> bool:
  sStack = []
  tStack = []

  sLen = len(s)
  tLen = len(t)

  for i in range(max(sLen, tLen)):
    if i < sLen:
      if s[i] == '#' and sStack:
        sStack.pop()
      elif s[i] != '#':
        sStack.append(s[i])
    
    if i < tLen:
      if t[i] == '#' and tStack:
        tStack.pop()
      elif t[i] != '#':
        tStack.append(t[i])

  return sStack == tStack




print(backspaceCompare('ab#c', 'ad#c'))
print(backspaceCompare('ab##', 'c#d#'))
print(backspaceCompare('a#c', 'b'))
print(backspaceCompare('y#fo##f', 'y#f#o##f'))
