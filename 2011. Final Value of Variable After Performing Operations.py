operations = ["--X","X++","X++"]
x = 0

for operation in operations:
  if operation == "X++" or operation == "++X":
    x += 1
  else:
    x -= 1

print(x)