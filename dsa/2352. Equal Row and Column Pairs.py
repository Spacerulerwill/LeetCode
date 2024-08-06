# https://leetcode.com/problems/equal-row-and-column-pairs/

from collections import Counter

class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        total = 0
        row_counts = Counter(tuple(row) for row in grid)
        col_counts = Counter(tuple(grid[row_idx][col_idx] for row_idx in range(n)) for col_idx in range(n))
        for val, count in row_counts.items():
            if val in col_counts:
                total += count * col_counts[val]
        return total




if __name__ == "__main__":
    solution = Solution()
    print(solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

