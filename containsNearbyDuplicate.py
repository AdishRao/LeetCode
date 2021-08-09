#https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dnums = {}
        
        for i,num in enumerate(nums):
            if num in dnums:
                if (i-dnums[num]) <= k:
                    return True
            dnums[num] = i
            
        return False