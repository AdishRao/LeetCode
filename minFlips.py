# https://leetcode.com/problems/bulb-switcher-iv/
class Solution:
    def minFlips(self, target: str) -> int:
        if '1' not in target:
            return 0
        revstr = target[target.index('1'):][::-1]
        count = 0
        cur = revstr[0]
        for i in range(len(revstr)):
            if revstr[i]!=cur:
                count+=1
                cur = revstr[i]
        count+=1
        return count