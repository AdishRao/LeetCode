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