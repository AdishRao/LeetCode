#https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/
class Solution:
    def gcd(a, b):  
        if b%a==0:
            return a
        return gcd(b%a, a)

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        number_dict = {}
        for i in deck:
            if i in number_dict:
                number_dict[i]+=1
            else:
                number_dict[i]=1
        values = sorted(number_dict.values())
        g = values[0]
        for i in values[1:]:
            g = gcd(g,i)
            if g < 2:
                return False
        return True