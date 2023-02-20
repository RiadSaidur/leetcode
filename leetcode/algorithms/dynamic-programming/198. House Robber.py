from typing import List


class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]

    money = [*nums]
    money[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        money[i] = max(money[i-1], nums[i] + money[i-2])

    return money[-1]