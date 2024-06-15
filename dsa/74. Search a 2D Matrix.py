# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        low = 0
        high = (rows * cols) - 1
        while low <= high:
            mid = (low + high)//2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] == target:
                return True
            elif target > matrix[r][c]:
                low = mid + 1
            else:
                high = mid - 1
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))