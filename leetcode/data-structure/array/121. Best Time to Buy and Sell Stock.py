from typing import List

prices1 = [7,1,5,3,6,4]
prices2 = [7,6,4,3,1]
prices3 = [0]
prices4 = [2,1]
prices5 = [1,2,4]
prices6 = [2,4,1]
prices7 = [3,2,6,5,0,3]
prices8 = [2,1,2,1,0,1,2]

def maxProfit(prices: List[int]) -> int:
  minBuyDay = 0
  maxSellDay = 1

  if len(prices) == 1:
    return 0

  profit = prices[maxSellDay] - prices[minBuyDay]

  for day in range(1, len(prices)):
    if prices[minBuyDay] > prices[day] and day != len(prices) - 1:
      minBuyDay = day
    elif prices[maxSellDay] < prices[day]:
      maxSellDay = day
    
    if maxSellDay <= minBuyDay and minBuyDay != len(prices) - 1:
      maxSellDay = minBuyDay + 1
    profit = max(profit, prices[maxSellDay] - prices[minBuyDay])
  
  return max(profit, 0)

print(maxProfit(prices=prices1))
print(maxProfit(prices=prices2))
print(maxProfit(prices=prices3))
print(maxProfit(prices=prices4))
print(maxProfit(prices=prices5))
print(maxProfit(prices=prices6))
print(maxProfit(prices=prices7))
print(maxProfit(prices=prices8))