# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dnums = {}
        for num in nums:
            if num in dnums:
                dnums[num]+=1
            else:
                dnums[num]=1
                
        for key, value in dnums.items():
            if value!=2:
                return key