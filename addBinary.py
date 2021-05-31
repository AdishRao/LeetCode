#https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = '0b' + a
        b = '0b' + b
        c = bin(int(a,2)+int(b,2))[2:]
        return(c)