#https://leetcode.com/problems/min-cost-climbing-stairs/

#Tabulization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2,len(cost)):
            dp[i] = cost[i] + min(dp[i-1],dp[i-2])
            
        print(dp)
        return min(dp[-1],dp[-2])

#Memoization
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def cal_cost(n,cost,memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return cost[0]
            if n == 1:
                return cost[1]
            
            ret_cost = min(cal_cost(n-1, cost, memo), cal_cost(n-2, cost, memo))
            
            mycost = ret_cost + cost[n]
            
            memo[n] = mycost
            return mycost
        
        cost.append(0)
        return cal_cost(len(cost)-1,cost, {})