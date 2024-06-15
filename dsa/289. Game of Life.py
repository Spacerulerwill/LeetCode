# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # Encoding:
        # 0 - dead, haven't been visited yet
        # 1 - alive, haven't been visited yet
        # 2 - dead this generation, alive next generation
        # 3 - alive this generation, dead next generation
        # 5 - alive this generation, alive next generation

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                current_cell = board[r][c]
                
                # Extract boolean evaluations to avoid repetition
                above = r > 0
                below = r < rows - 1
                left = c > 0
                right = c < cols - 1
                
                # Count live neighbours
                alive_neighbours = 0
                alive_neighbours += int(above and board[r-1][c] & 1 == 1)
                alive_neighbours += int(below and board[r+1][c] & 1 == 1)
                alive_neighbours += int(left and board[r][c-1] & 1 == 1)
                alive_neighbours += int(right and board[r][c+1] & 1 == 1)
                alive_neighbours += int(above and left and board[r-1][c-1] & 1 == 1)
                alive_neighbours += int(below and left and board[r+1][c-1] & 1 == 1)
                alive_neighbours += int(above and right and board[r-1][c+1] & 1 == 1)
                alive_neighbours += int(below and right and board[r+1][c+1] & 1 == 1)

                if current_cell == 0:
                    if alive_neighbours == 3:
                        board[r][c] = 2
                else:
                    if alive_neighbours < 2 or alive_neighbours > 3:
                        board[r][c] = 3
                    else:
                        board[r][c] = 5

        for r in range(rows):
            board[r] = [1 if board[r][c] in {2, 5} else 0 for c in range(cols)]

        
if __name__ == "__main__":
    board = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0]
    ]
    solution = Solution()
    solution.gameOfLife(board)
