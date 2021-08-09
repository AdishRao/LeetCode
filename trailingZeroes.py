#https://leetcode.com/problems/factorial-trailing-zeroes/

#Brute Force
class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 1
        while(n!=0):
            res*=n
            n-=1
        res = str(res)
        
        count = 0
        for i in range(len(res)-1,-1,-1):
            if res[i] != '0':
                break
            count+=1
        return count


#Math
class Solution:
    def trailingZeroes(self, n: int) -> int:
    
        if n == 0:
            return 0
        else: 
            return n // 5 + self.trailingZeroes(n // 5)