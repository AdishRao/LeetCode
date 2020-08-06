#https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        numbered_words = []
        for word in words:
            num = []
            for i in word:
                num.append(order.index(i))
            numbered_words.append(num)
        return(sorted(numbered_words)==numbered_words)