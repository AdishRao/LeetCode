#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_ = prices[0]
        max_ = 0
        
        for i in range(1,len(prices)):
            if prices[i] < min_:
                min_ = prices[i]
            elif (prices[i] - min_)>max_:
                max_ = prices[i] - min_
        return max_