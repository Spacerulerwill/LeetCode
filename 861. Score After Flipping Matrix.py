# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        score = 0
        # flip rows if start with zero
        for r in range(rows):
            if grid[r][0] == 0:
                for c in range(cols):
                    grid[r][c] = 1 - grid[r][c]
        # flip cols if more zeros than ones
        for c in range(cols):
            zeros = 0
            # count zeros in row
            for r in range(rows):
                if grid[r][c] == 0:
                    zeros += 1
            # flip if greater than half of them
            if zeros > rows - zeros:
                for r in range(rows):
                    grid[r][c] = 1 - grid[r][c]
            # increment score
            for r in range(rows):
                if grid[r][c] == 1:
                    score += (1 << (cols-c-1))
        return score

if __name__ == "__main__":
    solution = Solution()
    print(solution.matrixScore([
        [0,0,1,1],
        [1,0,1,0],
        [1,1,0,0]
    ]))