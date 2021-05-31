#https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        def cal_fib(n,memo):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            memo[n] = cal_fib(n-1,memo) + cal_fib(n-2,memo)
            return memo[n]
        
        return cal_fib(n, {})