import collections
import math
import time
from typing import List


tasks = [2,2,3,3,2,4,4,4,4,4]
tasks2 = [2,3,3]
tasks3 = [5,5,5,5]
tasks4 = [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69]

def minimumRounds(tasks: List[int]) -> int:
  days = 0
  taskLeft = collections.Counter(tasks)
  
  for task in taskLeft.values():
    if(task == 1):
      return -1
    
    days += math.ceil(task/3)
      
  return days

def minimumRoundsBest(tasks: List[int]) -> int:
  days = 0
  taskLeft = collections.Counter(tasks)
  
  for task in taskLeft.values():
    if(task == 1):
      return -1
    
    days += task//3
    if task%3:
      days += 1
      
  return days

# print(minimumRounds(tasks))
# print(minimumRounds(tasks2))
# print(minimumRounds(tasks3))
# print(minimumRounds(tasks4))

start = time.time()
for i in range(9999):
  minimumRounds(tasks)
  minimumRounds(tasks2)
  minimumRounds(tasks3)
  minimumRounds(tasks4)
print(time.time() - start)

start = time.time()
for i in range(9999):
  minimumRoundsBest(tasks)
  minimumRoundsBest(tasks2)
  minimumRoundsBest(tasks3)
  minimumRoundsBest(tasks4)
print(time.time() - start)