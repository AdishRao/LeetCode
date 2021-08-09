#https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        len_ = len(s)
        l = 0
        h = len_ - 1
        vowels = 'aeiouAEIOU'
        s = list(s)
        print(s)
        i = 0
        while(l<h):
            if (s[l] in vowels and s[h] in vowels):
                s[l], s[h] = s[h], s[l]
                l+=1
                h-=1
            while(l<len_ and (not s[l] in vowels)):
                l+=1
            while(h>-1 and (not s[h] in vowels)):
                h-=1
        
        return ''.join(s)