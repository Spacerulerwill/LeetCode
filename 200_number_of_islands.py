class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def fill_island(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            fill_island(r + 1, c)
            fill_island(r, c + 1)
            fill_island(r - 1, c)
            fill_island(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    fill_island(r, c)
        return islands


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.numIslands(
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
