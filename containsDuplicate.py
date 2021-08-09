#https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dnum = {}
        
        for num in nums:
            if num in dnum:
                return True
            dnum[num] = 1
            
        return False