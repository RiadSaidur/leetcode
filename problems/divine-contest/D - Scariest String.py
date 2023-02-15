"""
INCOMPLETE
"""

def is_scary(subseq):
  n = len(subseq)
  if n % 2 != 0: 
    return False

  half = n // 2

  if subseq[:half] != subseq[half:]: 
    return False

  return True

def find_scariest_costumes(costumes):
  max_scary = []

  for i in range(len(costumes)):
    for j in range(i+2, len(costumes)+1, 2): 
      subseq = costumes[i:j]

      if is_scary(subseq) and subseq > max_scary: 
        max_scary = subseq

  return list(max_scary)

costumes = [3, 1, 2, 3, 2, 3, 3, 3]
scariest = find_scariest_costumes(costumes)
print(scariest)