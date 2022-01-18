class Solution(object):
  def decode(self, encoded, first):
    """
    :type encoded: List[int]
    :type first: int
    :rtype: List[int]
    """
    ans = [first]

    for code in encoded:
      ans.append(first^code)
      first = ans[-1]
    
    return ans