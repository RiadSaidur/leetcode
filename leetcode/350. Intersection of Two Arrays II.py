import collections
import time
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
  if not nums1 or not nums2:
    return []

  map1 = collections.Counter(nums1)

  result = []

  for num in nums2:
    if num in map1 and map1[num]:
      result.append(num)
      map1[num] -= 1
  
  return result

def sortedIntersect(nums1: List[int], nums2: List[int]) -> List[int]:
  if not nums1 or not nums2:
    return []

  nums1 = sorted(nums1)
  nums2 = sorted(nums2)

  result = []

  i = 0
  j = 0

  while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
      result.append(nums1[i])
      i += 1
      j += 1
    elif nums1[i] > nums2[j]:
      j += 1
    elif nums1[i] < nums2[j]:
      i += 1
    
  return result
      
def afterSortedIntersect(nums1: List[int], nums2: List[int]) -> List[int]:
  if not nums1 or not nums2:
    return []

  result = []

  i = 0
  j = 0

  while i < len(nums1) and j < len(nums2):
    if nums1[i] == nums2[j]:
      result.append(nums1[i])
      i += 1
      j += 1
    elif nums1[i] > nums2[j]:
      j += 1
    elif nums1[i] < nums2[j]:
      i += 1
    
  return result

start = time.time()
for i in range(99999):
  intersect([1,2,2,1], [2,2])
  intersect([4,9,5], [9,4,9,8,4])
print('intersect', time.time() - start)

start = time.time()
for i in range(99999):
  sortedIntersect([1,1,2,2], [2,2])
  sortedIntersect([4,5,9], [4,4,8,9])
print('sortedIntersect', time.time() - start)

start = time.time()
for i in range(99999):
  afterSortedIntersect([1,2,2,1], [2,2])
  afterSortedIntersect([4,9,5], [9,4,9,8,4])
print('afterSortedIntersect', time.time() - start)