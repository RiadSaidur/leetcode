class Solution(object):
  def maximumWealth(self, accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    maxWealth = 0

    for account in accounts:
      wealth = sum(account)
      if wealth > maxWealth:
        maxWealth = wealth
        
    return maxWealth