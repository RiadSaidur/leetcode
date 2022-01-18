# Question-3:
# Suppose you are given a list of integers. Your final task is to return a 
# list that will contain the values in the following format:
# [Largest, Smallest, Second largest, Second smallest,...so on...]

# Write a function named weird_sort() which will receive a list on calling 
# and then RETURN another list which will follow the format mentioned above. 
# Then print the list that was returned from the function. You can assume the 
# length of the given list will always be even, there will be no duplicate 
# values, and the values will be in range(0,101).
# ================================================
# Function Call 01:
# weird_sort([9, 3, 5, 7, 16, 20])

# Sample Output 01:
# [20, 3, 16, 5, 9, 7]

# Function Call 02:
# weird_sort([10,20,30,40,50,60])
# ================================================
# Sample Output 02:
# [60, 10, 50, 20, 40, 30]

from typing import List


def weird_sort(items: List[int]):
  sorted_items = sorted(items, reverse=True)
  weird_sorted = []

  for i in range(int(len(sorted_items)/2)):
    weird_sorted.append(sorted_items[i])
    weird_sorted.append(sorted_items[-i-1])

  print(weird_sorted)


weird_sort([9, 3, 5, 7, 16, 20])
weird_sort([10,20,30,40,50,60])