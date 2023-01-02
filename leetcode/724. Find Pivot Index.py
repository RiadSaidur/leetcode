# nums = [1,2,3]
nums = [1,7,3,6,5,6]
# nums = [2,1,-1]
# nums = [1,2,5,6]

def pivotIndex(nums):
  leftSum = 0
  rightSum = sum(nums)

  for idx, num in enumerate(nums):
    rightSum = rightSum - num

    if leftSum == rightSum:
      return idx
    
    leftSum = leftSum + num
  
  return -1

print(pivotIndex(nums=nums))
