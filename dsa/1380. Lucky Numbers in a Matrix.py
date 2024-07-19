# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        max_cols = [0 for _ in range(cols)]
        min_rows = [0 for _ in range(rows)]
        for col in range(cols):
            _max = 0
            for row in range(rows):
                _max = max(_max, matrix[row][col])
            max_cols[col] = _max
        for row in range(rows):
            _min = float("inf")
            for col in range(cols):
                _min = min(_min, matrix[row][col])
            min_rows[row] = _min
        return [a for a in max_cols for b in min_rows if a == b]



if __name__ == "__main__":
    solution = Solution()
    print(solution.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))