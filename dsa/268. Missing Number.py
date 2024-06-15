# https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        maxElem = len(nums)
        sumToMax = (maxElem * (maxElem + 1)) // 2
        return sumToMax - sum(nums)
    
if __name__ == "__main__":
    solution = Solution()
    print(
        solution.missingNumber([0,1,3,4]),
        solution.missingNumber([0,1,2,3,7,8,9,5,6]),
        solution.missingNumber([0,5,4,3,7,8,9,1,6])
    )