# https://leetcode.com/problems/sudoku-solver/

class Solution:    
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def is_valid(r: int, c: int, k: str) -> bool:
            not_in_row = k not in board[r]
            not_in_col = k not in (board[i][c] for i in range(9))
            box_x = c // 3
            box_y = r // 3 
            not_in_box = k not in (board[i][j] for i in range(box_y*3, (box_y*3)+3) for j in range(box_x * 3, (box_x * 3) + 3))
            return not_in_row and not_in_col and not_in_box
        
        def solve(r=0, c=0) -> bool:
            if r == 9:
                return True
            elif c == 9:
                return solve(r+1, 0)
            elif board[r][c] != ".":
                return solve(r, c+1)
            else:
                for k in range(1, 10):
                    if is_valid(r,c,str(k)):
                        board[r][c] = str(k)
                        if solve(r, c+1):
                            return True
                        else:
                            board[r][c] = "."
                # should never reach here, as it will always have a solution, but its good to have anyway
                return False
        solve()
        