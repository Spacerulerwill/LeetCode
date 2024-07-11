# https://leetcode.com/problems/surface-area-of-3d-shapes/

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        surface_area = 0
        for r in range(rows): 
            for c in range(cols):
                height = grid[r][c]
                if height > 0:
                    surface_area += 2
                for (dr, dc), check in [
                    ((-1, 0), lambda r, c: r > 0),
                    ((1, 0), lambda r, c: r < rows - 1),
                    ((0, -1), lambda r, c: c > 0),
                    ((0, 1), lambda r, c: c < cols - 1)
                ]:
                    if check(r, c):
                        other_height = grid[r + dr][c + dc]
                        if other_height < height:
                            surface_area += height - other_height
                    else:
                        surface_area += height                
        return surface_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.surfaceArea([[1,2],[3,4]]))
    print(solution.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))