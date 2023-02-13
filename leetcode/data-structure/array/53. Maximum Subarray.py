from typing import List


def maxSubArray(nums: List[int]) -> int:
  maxSum = nums[0]
  currSum = 0

  for num in nums:
    if currSum < 0:
      currSum = 0
    currSum += num
    maxSum = max(currSum, maxSum)

  return maxSum


print(maxSubArray([1]))
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))