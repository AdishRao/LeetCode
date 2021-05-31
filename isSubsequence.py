# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        len_ = len(s)
        for c in t:
            if ((i!=len_) and (s[i] == c)):
                i+=1
        if i==len_:
            return True
        return False

    
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def print_(dp):
            print("**")
            for i in range(len(dp)):
                for j in range(len(dp[0])):
                    print(dp[i][j], end = ' ')
                print(end='\n')
            
        m = len(s)
        n = len(t)
        dp = []
        for i in range(m+1):
            dp.append([])
            for j in range(n+1):
                dp[i].append(None)
        print_(dp)
        for i in range(m+1):
            dp[i][0] = False
        for i in range(n+1):
            dp[0][i] = True
        print_(dp)
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s[i-1] == t[j-1]):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
                    
        print_(dp)
        return dp[-1][-1]