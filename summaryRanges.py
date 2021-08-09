#https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return nums
        start = nums[0]
        cur = start
        res = []
        for num in nums[1:]:
            if num!=(cur+1):
                if cur!=start:
                    res.append(str(start)+"->"+str(cur))
                else:
                    res.append(str(start))
                start = num
                cur = num
            else:
                cur = num
        
        if nums[-1]==start:
            res.append(str(start))
        else:
            res.append(str(start)+"->"+str(cur))
        
        return res