# https://leetcode.com/problems/running-sum-of-1d-array/description/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res = [0 for _ in range(len(nums))]
        sum = 0
        for idx, num in enumerate(nums):
            sum += num
            res[idx] = sum
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSum([1,2,3,4]))