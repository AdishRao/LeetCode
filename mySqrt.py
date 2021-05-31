#https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        mid = 0
        high = x
        prev = 0
        
        while(low < high):
            mid = (low+high)//2
            sq = mid*mid
            if(sq == x):
                return mid
            elif(sq>x):
                high = mid - 1
            else:
                low = mid + 1
        if (low*low <= x):
            return low
        return low-1