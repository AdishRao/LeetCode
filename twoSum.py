#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for (i,num) in enumerate(nums):
            rem = target - num
            if rem in remainder:
                return [remainder[rem],i]
            else:
                remainder[num] = i
        raise Exception("Sorry, no Solution")