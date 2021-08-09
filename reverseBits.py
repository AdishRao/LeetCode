#https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        rev = bin(n)[2:]
        rem = 32 - len(rev)
        rem = '0b' + ("0"*rem + rev)[::-1]
        
        rev = int(rem,2)
        return rev