from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  result = []

  for i in range(len(intervals)):
    if newInterval[1] < intervals[i][0]:
      result.append(newInterval)
      return result + intervals[i:]
    elif newInterval[0] > intervals[i][1]:
      result.append(intervals[i])
    else:
      newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
  
  result.append(newInterval)

  return result

print(insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
# print(insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
