#https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        
        for c in magazine:
            magazine_dict[c] = magazine_dict.get(c,0) + 1
            
        for c in ransomNote:
            count = magazine_dict.get(c,0)
            
            if count == 0:
                return False
            
            magazine_dict[c] -= 1
            
        return True