# https://leetcode.com/problems/prefix-and-suffix-search/

class WordFilter:
    words_dict = {}

    def __init__(self, words: List[str]):
        for i in range(len(words)):
            word = words[i]
            lenw = len(word)
            for j in range(lenw):
                for k in range(lenw):
                    hash_word = word[-j:]+'#'+word[:lenw-k]
                    self.words_dict[hash_word] = i

    def f(self, prefix: str, suffix: str) -> int:
        find_word = suffix+'#'+prefix
        if find_word in self.words_dict:
            return self.words_dict[find_word]
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
