#https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = {}
        for char in s:
            if char in letters:
                letters[char]+=1
            else:
                letters[char]=1
        flag = False 
        ret = 0
        for value in letters.values():
            ret += (value//2)*2
            if not flag and value%2 !=0:
                flag = True
        if flag:
            ret+=1
            
        return ret