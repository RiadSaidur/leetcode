from typing import List


def letterCasePermutation(s: str) -> List[str]:
  result = ['']
  for char in s:
    if char.isalpha():
      result = [i+j for i in result for j in [char.upper(), char.lower()]]
    else:
      result = [i+char for i in result]
  return result