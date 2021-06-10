#https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        len_ = len(s)
        i = 0
        j = len_ - 1
        s = s.lower()
        while(i<j):
            while(i<len_ and not s[i].isalnum()):
                i+=1
            while(j>=0 and not s[j].isalnum()):
                j-=1
            
            if(i>j):
                break
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
            
        return True