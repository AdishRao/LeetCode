#https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        def climbs(n, memo):
            if n in memo:
                return memo[n]
            if (n == 0 or n == 1):
                return 1
            memo[n] = climbs(n-1, memo) + climbs(n-2, memo)
            return memo[n]
        
        return climbs(n, {})