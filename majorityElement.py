#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_ = 0
        ret_ = nums[0]
        snums = set(nums)
        
        for i in snums:
            c = nums.count(i)
            if c > (len(nums)//2):
                return i