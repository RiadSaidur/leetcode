def isSubsequence(s: str, t: str) -> bool:
  if(not s): return True
  if(not t): return False

  for _, char in enumerate(s):
    currentSubIdx = t.find(char)
    t = t[currentSubIdx+1:]
    if(currentSubIdx == -1): return False
  
  return True

# BEST SOLUTION
# def isSubsequence(s: str, t: str) -> bool:
#   for i in range (0, len(s)):    
#     try:
#       index = t.index(s[i])
#     except ValueError: 
#       return False

#     t = t[index+1:]

#   return True


print(isSubsequence('abc', 'ahbgdc'))
print(isSubsequence('abc', 'bhagdc'))
print(isSubsequence('axc', 'ahbgdc'))
print(isSubsequence('aaaaaa', 'bbaaaa'))
print(isSubsequence('', 'ahbgdc'))
print(isSubsequence('b', 'abc'))