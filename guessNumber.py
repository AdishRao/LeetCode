#https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        h = n
        while(True):
            m = (l+h)//2
            ans = guess(m)
            
            if ans == 0:
                return m
            elif ans<0:
                h = m-1
            else:
                l = m+1
            