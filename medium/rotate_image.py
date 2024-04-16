# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        # transpose
        for row in range(rows):
            for col in range(row+1, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        # flip      
        for row in range(rows):
            for col in range(cols//2):
                matrix[row][col], matrix[row][cols-col-1] = matrix[row][cols-col-1], matrix[row][col]
    
if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    for row in matrix:
        print(row)
    solution.rotate(matrix)
    for row in matrix:
        print(row)
    