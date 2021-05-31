#https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current = 0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[current] = nums[i]
                current+=1
        return current