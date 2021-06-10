#https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        
        for i in range(1,rowIndex+1):
            triangle.insert(i,[1,1])
            
            for j in range(1,i):
                insert = triangle[i-1][j-1] + triangle[i-1][j]
                triangle[i].insert(j,insert)
                
        return triangle[rowIndex]