#https://leetcode.com/problems/divisor-game/

class Solution:
    def divisorGame(self, n: int) -> bool:
        d = [False] * (n+1) #DP where dp[i] represents result for game i
        for i in range(2, n+1): #taking all games > 1 till n our required game
            for j in range(1, i//2 + 1): #check for all divisors from 1 till largest diviser, ie. i//2
                if i % j == 0 and not d[i-j]: #if it is a divisor (possible move) and if this move is taken, check if opponent can win,result of dp[current game - move taken], which is the game dp[i-j] for opponent
                    d[i] = True #since the game at dp[i-j] is not winnable, the game from i taking move j is winnable
                    break
        return d[n]