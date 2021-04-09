# https://leetcode.com/problems/battleships-in-a-board/
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        Number_Of_Ships = 0
        row_len = len(board)
        col_len = len(board[0])
        for row in range(row_len):
            for col in range(col_len):
                if board[row][col] == 'X':
                    if (col == 0 or board[row][col-1] != 'X') and (row == 0 or board[row-1][col] != 'X'):
                        Number_Of_Ships += 1

        return Number_Of_Ships