from typing import List

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,6,5]
n = 5

# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums2 = [0]
# n = 0
# nums1 = [1]
# # m = 1

# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 6
# nums2 = [1,2,2]
# n = 3

# nums1 = [-1,-1,0,0,0,0]
# m = 4
# nums2 = [-1,0]
# n = 2

# nums1 = [1,0]
# m = 1
# nums2 = [2]
# n = 1

nums1 = [1,5,8,0,0,0,0,0]
m = 3
nums2 = [-1,2,2,4,6]
n = 5

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  last = m+n-1

  while m > 0 and n > 0:
    if nums1[m-1] > nums2[n-1]:
      nums1[last] = nums1[m-1]
      m -= 1
    else:
      nums1[last] = nums2[n-1]
      n -= 1
    last -= 1

  while n > 0:
    nums1[last] = nums2[n-1]
    n -= 1
    last -= 1



  


merge(nums1, m, nums2, n)
print(nums1)