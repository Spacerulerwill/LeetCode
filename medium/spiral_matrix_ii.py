# https://www.youtube.com/watch?v=Scy7kFa47hg

class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]

        top = -1
        bottom = n
        left = -1
        right = n
        
        row = 0
        col = -1

        i = 1
        while True:
            # go left
            while col < right - 1:
                col += 1
                result[row][col] = i
                i += 1
            if not (left < right - 1 and top < bottom - 1):
                break
            top += 1

            # go down
            while row < bottom - 1:
                row += 1
                result[row][col] = i
                i += 1
            right -= 1
            if not (left < right - 1 and top < bottom - 1):
                break

            # go right
            while col > left + 1:
                col -= 1
                result[row][col] = i
                i += 1
            if not (left < right - 1 and top < bottom - 1):
                break
            bottom -= 1

            # go up
            while row > top + 1:
                row -= 1
                result[row][col] = i
                i += 1
            if not (left < right - 1 and top < bottom - 1):
                break
            left += 1
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.generateMatrix(3))
    print(solution.generateMatrix(1))