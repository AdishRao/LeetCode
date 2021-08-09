#https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 0:
            max_pow_3 = 3**19 #(3**20 > 2**31 - 1) works for all prime numbers
            return (max_pow_3 % n) == 0