#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0 or l == 1:
            return l
        i,j = 0,1
        while j!= l:
            if nums[i]!=nums[j]:
                j+=1
                i+=1
            else:
                while(j!=l and nums[i]==nums[j]):
                    j+=1
                if(j!=l):
                    i+=1
                    nums[i] = nums[j]
        return (i+1)