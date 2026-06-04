class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      max_profit = 0
      min_price = prices[0]

      for price in prices[1:]:
        
        
        curr_profit = price - min_price
        if curr_profit > max_profit:
          max_profit = curr_profit
        if price < min_price:
          min_price = price

      return max_profit
