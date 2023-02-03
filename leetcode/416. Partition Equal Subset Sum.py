from typing import List


def canPartition(nums: List[int]) -> bool:
  if sum(nums) % 2:
    return False

  sumSet = set([0])

  target = sum(nums) // 2

  for i in range(len(nums)-1, -1, -1):
    currSumSet = set()

    for num in sumSet:
      if num + nums[i] == target:
        return True
      
      currSumSet.add(num + nums[i])
      currSumSet.add(num)
    
    sumSet = currSumSet
  
  return False


# print(canPartition([1,5,11,5]))
# print(canPartition([1,2,3,5]))
# print(canPartition([1,3,4,4]))
print(canPartition([2,2,1,1]))
    