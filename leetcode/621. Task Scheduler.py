import collections
from heapq import heapify
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
  if n == 0:
    return len(tasks)

  taskFrequency = list(collections.Counter(tasks).values())
  
  cycle = 0
  
  while taskFrequency:
    i = 0
    taskFrequency.sort(reverse=True)
    for _ in range(n+1):
      cycle += 1
      
      if i < len(taskFrequency) and taskFrequency[i] != 0:
        taskFrequency[i] -= 1
        if taskFrequency[i] == 0:
          taskFrequency.pop(i)
          i -= 1

      # print(cycle, ':', taskFrequency)

      if not len(taskFrequency):
        return cycle
      i += 1

    # print('-'*25)

print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
print(leastInterval(tasks = ["A","A","B","B","B"], n = 2))
print(leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
print(leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))
print(leastInterval(tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], n = 2))
