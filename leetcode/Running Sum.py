nums = [1,2,3,4]

runningSum = []

for idx, num in enumerate(nums):
  runningSum.append(sum(nums[:idx+1]))

print(runningSum)
    