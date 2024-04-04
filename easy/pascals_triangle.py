# https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = [[1]]
        
        for rowIndex in range(1, numRows):
            prevRow = rows[-1]
            newRow = [1]
            
            for i in range(1, len(prevRow)):
                newRow.append(prevRow[i-1] + prevRow[i])
            
            newRow.append(1)
            rows.append(newRow)
        
        return rows
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.generate(15))