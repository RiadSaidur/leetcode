from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
  nums.sort()
  result = nums[0]+nums[1]+nums[2]

  for i in range(len(nums)-2):
    j, k = i+1, len(nums)-1
    while j < k:
      total = nums[i]+nums[j]+nums[k]
      
      if abs(total-target) < abs(result-target):
        result = total

      if total == target:
        return total
      elif total < target:
        j += 1
      else:
        k -= 1

  return result

print(threeSumClosest(nums = [-1,2,1,-4], target = 1))