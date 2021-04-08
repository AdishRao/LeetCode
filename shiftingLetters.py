#https://leetcode.com/problems/shifting-letters/submissions/
class Solution:
    base = ord('a')
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        len_shift = len(shifts)
        shift_val = sum(shifts)
        ret_val = ''
        for i in range(len_shift):
            ret_val+= self.apply_shift(ord(S[i]), shift_val)
            shift_val -= shifts[i]
        return ret_val
    
    def apply_shift(self, ascii_val, shift):
        return chr((ascii_val - self.base + shift)%26 + self.base)
              