class MyQueue:

  def __init__(self):
    self.mainStack = []
    self.subStack = []

  def push(self, x: int) -> None:
    while self.mainStack:
      self.subStack.append(self.mainStack.pop())

    self.mainStack.append(x)

    while self.subStack:
      self.mainStack.append(self.subStack.pop())

  def pop(self) -> int:
    return self.mainStack.pop()      

  def peek(self) -> int:
    return self.mainStack[-1]

  def empty(self) -> bool:
    return not self.mainStack