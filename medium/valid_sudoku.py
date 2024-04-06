# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # rows
        for row in board:
            seen = set()
            for elem in row:
                if elem != ".":
                    if elem in seen:
                        return False
                    else:
                        seen.add(elem)
        # columns
        for i in range(9):
            column = [row[i] for row in board]
            seen = set()
            for elem in column:
                if elem != ".":
                    if elem in seen:
                        return False
                    else:
                        seen.add(elem)
        
        for box_x in range(3):
            for box_y in range(3):
                seen = set()
                box = [board[(box_x * 3) + i // 3][(box_y * 3) + i % 3] for i in range(9)]
                for elem in box:
                    if elem != ".":
                        if elem in seen:
                            return False
                        else:
                            seen.add(elem) 
        return True