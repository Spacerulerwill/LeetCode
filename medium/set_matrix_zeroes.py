# https://leetcode.com/problems/set-matrix-zeroes/
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        for row in matrix:
            print(row)
        rows = [False for _ in range(len(matrix))]
        cols = [False for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows[row] = True
                    cols[col] = True
        print(rows)
        print(cols)
        for idx, should_zero in enumerate(rows):
            if should_zero:
                matrix[idx] = [0 for _ in range(len(matrix[0]))]
        
        for idx, should_zero in enumerate(cols):
            if should_zero:
                for i in range(len(matrix)):
                    matrix[i][idx] = 0
        for row in matrix:
            print(row)
if __name__ == "__main__":
    solution = Solution()
    print(solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))