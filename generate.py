#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        
        for i in range(1,numRows):
            triangle.insert(i,[1,1])
            
            for j in range(1,i):
                insert = triangle[i-1][j-1] + triangle[i-1][j]
                triangle[i].insert(j,insert)
                
        return triangle