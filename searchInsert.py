#https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_ = len(nums)
        high = len_-1
        low = 0
    
        while(low<high):
            n = (low+high)//2 
            if nums[n] == target:
                return n
            if nums[n] > target:
                high = n-1
            else:
                low = n+1

        if target > nums[low]:
            return low + 1
        else:
            return low