#https://leetcode.com/problems/length-of-last-word/

#Faster
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.strip().split(' ')
        return len(l[-1])

#Slower        
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_ = 0
        
        s = s.strip()
        for c in s:
            if c==' ':
                len_ = 0
                continue
            len_+=1
        return len_