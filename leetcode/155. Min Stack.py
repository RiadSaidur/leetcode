class MinStack:

  def __init__(self):
    self.stack = []
    self.minStack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    if not self.minStack:
      self.minStack.append(val)
    else:
      self.minStack.append(min(self.minStack[-1], val))

  def pop(self) -> None:
    self.stack.pop()
    self.minStack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.minStack[-1]
        


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-1)
print(minStack.getMin())
print(minStack.top())
# minStack.pop()
# print(minStack.getMin())