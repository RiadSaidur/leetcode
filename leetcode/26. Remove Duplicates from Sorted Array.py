from typing import List

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicates(nums: List[int]) -> int:
  nums[:] = sorted(set(nums))
  return len(nums)

print(removeDuplicates(nums=nums1))
print(removeDuplicates(nums=nums2))