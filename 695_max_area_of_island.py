class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        _max = 0
        rows = len(grid)
        cols = len(grid[0])

        def island_area(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (
                1
                + island_area(r + 1, c)
                + island_area(r, c + 1)
                + island_area(r - 1, c)
                + island_area(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = island_area(r, c)
                    _max = max(_max, area)
        return _max


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxAreaOfIsland(
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ]
        )
    )
