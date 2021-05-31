#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        nums = {n:1}
        while(n!=1):
            n = list(str(n))
            n = sum([int(x)**2 for x in n])
            if n in nums:
                return False
            else:
                nums[n] = 1
        return True

#############################
import functools

class Solution:
    def addDigits(self, num: int) -> int:
        while(num>=10):
            num = int(functools.reduce(lambda a,b : str(int(a)+int(b)), str(num)))
            
        return num