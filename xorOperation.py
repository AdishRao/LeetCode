# https://leetcode.com/problems/xor-operation-in-an-array/
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        n1 = start
        ret = n1
        for i in range(1,n):
            n2 = start+2*i
            ret = ret ^ n2
        return ret