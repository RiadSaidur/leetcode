class Solution(object):
  def minCostToMoveChips(self, position):
    """
    :type position: List[int]
    :rtype: int
    """
    odds = evens = 0

    for pos in position:
      if pos % 2:
        odds += 1
      else:
        evens += 1

    return min(odds, evens)
    