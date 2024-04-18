# https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += int(c == 0 or (c > 0 and grid[r][c-1] == 0))
                    perimeter += int(c == cols-1 or (c < cols-1 and grid[r][c+1] == 0))
                    perimeter += int(r == 0 or (r > 0 and grid[r-1][c] == 0))
                    perimeter += int(r == rows-1 or (r < rows-1 and grid[r+1][c] == 0))

        return perimeter
if __name__ == "__main__":
    solution = Solution()
    print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(solution.islandPerimeter([[1]]))
    print(solution.islandPerimeter([[1,0]]))