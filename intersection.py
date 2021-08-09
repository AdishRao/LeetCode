#https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            if i not in d:
                d[i] = True
                
        res = set()
        for i in nums2:
            if i in d:
                res.add(i)
                
        return res