#https://leetcode.com/problems/water-bottles/
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret_value = numBottles
        empty = 0
        while((numBottles+empty)>=numExchange):
            empty += numBottles
            numBottles=empty//numExchange
            empty = (empty%numExchange)
            ret_value+=numBottles
        return ret_value