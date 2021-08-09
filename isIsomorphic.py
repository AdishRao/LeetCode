#https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps1 = {}
        maps2 = {}
        
        for (c1,c2) in zip(s,t):
            if c1 in maps1:
                if maps1[c1] != (c1,c2):
                    return False
                
            if c2 in maps2:
                if maps2[c2] != (c1,c2):
                    return False
                
            maps1[c1] = (c1,c2)
            maps2[c2] = (c1,c2)
                
        return True
        