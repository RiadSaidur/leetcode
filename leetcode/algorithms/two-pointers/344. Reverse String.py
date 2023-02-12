from typing import List


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s)-1

    while left < right:
      s[left], s[right] = s[right], s[left]
      left, right = left+1, right-1

print(reverseString(s = ["h","e","l","l","o"]))
print(reverseString(s = ["H","a","n","n","a","h"]))