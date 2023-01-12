def isValid(s: str) -> bool:
  stack = []

  parentehesMap = {
    ')': '(',
    '}': '{',
    ']': '['
  }

  for char in s:
    if char in [')', '}', ']'] and stack:
      if parentehesMap.get(char) != stack[-1]:
        return False
      else:
        stack.pop()
    else:
      stack.append(char)
    
  if stack:
    return False
  else:
    return True


print(isValid("(({{[[()]]}}))]"))