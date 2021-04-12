# https://leetcode.com/problems/positions-of-large-groups/

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ret_val = []
        start = 0
        end = 0
        prev_char = s[0]
        
        for i in range(1,len(s)):
            if(s[i]!=prev_char):
                prev_char = s[i]
                end = i
                if ((end-start)>=3):
                    ret_val.append([start,end-1])
                start = i
        end = len(s)
        if ((end-start)>=3):
            ret_val.append([start,end-1]) 
        return ret_val