# https://leetcode.com/problems/word-pattern/
'''
The given definition of wordPattern redefines the str class object into a variable and thus I have used numeric
calculations to ensure the two patterns match
'''


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_dict = {}
        pattern_dict = {}
        str = str.split()
        if(len(str) != len(pattern)):
            return False
        str_res = 0
        pattern_res = 0
        num = 0
        for i in range(len(str)):
            if str[i] not in str_dict:
                str_dict[str[i]] = num
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = num
                num += 1
            str_res = (str_res*10) + str_dict[str[i]]
            pattern_res = (pattern_res*10) + pattern_dict[pattern[i]]

        return (pattern_res == str_res)


'''
Changing the definition of the class wordPattern from str -> stri
'''


class Solution:
    def wordPattern(self, pattern: str, stri: str) -> bool:
        str_dict = {}
        pattern_dict = {}
        stri = stri.split()
        if(len(stri) != len(pattern)):
            return False
        str_res = ''
        pattern_res = ''
        num = 0
        for i in range(len(stri)):
            if stri[i] not in str_dict:
                str_dict[stri[i]] = str(num)
            if pattern[i] not in pattern_dict:
                pattern_dict[pattern[i]] = str(num)
                num += 1
            str_res += str_dict[stri[i]]
            pattern_res += pattern_dict[pattern[i]]

        return (pattern_res == str_res)