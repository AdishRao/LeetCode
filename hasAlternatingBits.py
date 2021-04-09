# https://leetcode.com/problems/binary-number-with-alternating-bits/submissions/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        for i in range(len(bin_n)-1):
            if(bin_n[i] == bin_n[i+1]):
                return False
        return True