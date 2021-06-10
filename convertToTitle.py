#https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:        
        r = ''
        A = ord('A')
        while(columnNumber!=0):
            r = chr( A + (columnNumber-1)%26 ) + r
            columnNumber = (columnNumber-1)//26
        return(r)
        
        