#https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n > 0) and ((n & (n - 1)) == 0) and ((n & 0x55555555) == n)
        #check if n is +ve, check if n is a power of two, and finally check if the power of two is at an odd position