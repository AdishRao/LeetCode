#https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        h = num
        
        while(l<=h):
            m = (l+h)//2
            sq = m*m
            if sq == num:
                return True
            elif sq>num:
                h = m - 1
            else:
                l = m + 1
        return False
            