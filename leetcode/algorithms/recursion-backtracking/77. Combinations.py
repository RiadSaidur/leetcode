from typing import List


def combine(n: int, k: int) -> List[List[int]]:
  def dfs(nums, k, path, ret):
    if len(path) == k:
      ret.append(path)
      return 
    for i in range(len(nums)):
      dfs(nums[i+1:], k, path+[nums[i]], ret)

  combinations = []

  dfs(list(range(1, n+1)), k, [], combinations)

  return combinations


# print(combine(4,2))
# print(combine(1,1))
# print(combine(5,1))
# print(combine(3,1))
# print(combine(2,2))
print(combine(3,3))