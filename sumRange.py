#https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]*(len(nums)+1)
        self.sums[1] = nums[0]
        for i in range(2,len(nums)+1):
            self.sums[i] = self.sums[i-1] + nums[i-1] 

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right+1] - self.sums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)