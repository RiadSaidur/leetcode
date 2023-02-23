code = str(input())

num = ''

i = 0

while i < len(code):
  if code[i] == '-' and code[i+1] =='.':
    num += '1'
    i += 1
  elif code[i] == '-' and code[i+1] =='-':
    num += '2'
    i += 1
  elif code[i] == '.':
    num += '0'
  i += 1

print(num)