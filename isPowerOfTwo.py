#https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        Flag = False
        for c in bin(n):
            if c == '1':
                if Flag:
                    return False
                Flag = True
        
        return True