# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # edge case
        if len(matrix) == 1:
            return [x for x in matrix[0]]
        
        rows = len(matrix)
        cols = len(matrix[0])

        result = []
        top = -1
        bottom = rows
        left = -1
        right = cols
        
        row = 0
        col = -1

        while True:
            # go left
            while col < right - 1:
                col += 1
                result.append(matrix[row][col])            
            if not (left < right - 1 and top < bottom - 1):
                break
            top += 1

            # go down
            while row < bottom - 1:
                row += 1
                result.append(matrix[row][col])
            right -= 1
            if not (left < right - 1 and top < bottom - 1):
                break

            # go right
            while col > left + 1:
                col -= 1
                result.append(matrix[row][col])
            if not (left < right - 1 and top < bottom - 1):
                break
            bottom -= 1

            # go up
            while row > top + 1:
                row -= 1
                result.append(matrix[row][col])
            if not (left < right - 1 and top < bottom - 1):
                break
            left += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
