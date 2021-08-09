#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        for i in nums1:
            d[i] = d.get(i,0) + 1
            
        res = []
        for i in nums2:
            if i in d:
                if d[i] > 0:
                    res.append(i)
                    d[i] -= 1
                    
        return res