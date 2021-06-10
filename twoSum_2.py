#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        h = len(numbers)-1
        m = 0

        while(numbers[h]+numbers[l]>target):
            h-=1
            
        while(True):
            h1,l = h,0
            while(h1>=l):
                m  = (h1+l)//2
                sum_ = numbers[m] + numbers[h]
                if sum_ < target:
                    l = m+1
                elif sum_ > target:
                    h1 = m-1
                else:
                    return [m+1, h+1]
            h-=1