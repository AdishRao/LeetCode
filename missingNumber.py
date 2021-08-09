#https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_ = 0
        n = len(nums)
        
        for i in range(n):
            sum_-= nums[i]
            sum_+=i
        
        sum_+=n
        
        return (sum_)