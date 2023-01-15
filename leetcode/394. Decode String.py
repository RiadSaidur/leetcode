def decodeString(s: str) -> str:
  stack = []

  for char in s:
    print(stack)
    if char != ']':
      stack.append(char)
    else:
      substr = ''

      while stack[-1] != '[':
        substr = stack.pop() + substr
      stack.pop()

      n = ''
      while stack and stack[-1].isdigit():
        n = stack.pop() + n
      
      stack.append(int(n) * substr)
    
  return ''.join(stack)


# print(decodeString("3[a]2[bc]"))
print(decodeString("3[a2[c]]"))
# print(decodeString("2[abc]3[cd]ef"))