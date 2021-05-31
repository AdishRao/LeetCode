#https://leetcode.com/problems/longest-continuous-increasing-subsequence/s

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 0
        cur = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur+=1
            else:
                if cur > longest:
                    longest = cur
                cur = 1
        if cur > longest:
            longest = cur
        
        return longest