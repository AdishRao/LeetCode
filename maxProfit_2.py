#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ = prices[0]
        max_ = prices[0]
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] < min_:
                min_ = prices[i]
            else:
                profit += (prices[i] - min_)
                min_ = prices[i]
                
        return profit