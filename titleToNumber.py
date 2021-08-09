#https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        A = ord('A')        
        ret = 0
        
        for c in columnTitle:
            ret = (ret + (ord(c)-A+1))*26       
        ret //=26
        
        return(ret)