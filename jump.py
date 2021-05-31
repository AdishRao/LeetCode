#https://leetcode.com/problems/jump-game-ii/

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_position = 0
        current_position = -1
        for i in range(len(nums)):
            if max_position<len(nums)-1:
                if i>current_position:
                        jumps+=1
                        current_position = max_position
                if(i+nums[i]>max_position):
                    max_position = i+nums[i]
            else:
                break
        return jumps