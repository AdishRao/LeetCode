#https://leetcode.com/problems/counting-bits/

# DP Method
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        for i in range(1,n+1):
            if i%2 == 0:
                dp[i] = dp[i//2]
                continue
            dp[i] = dp[i//2] + 1
        return dp


#n*log(n)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(bin(i).count('1'))
        return res