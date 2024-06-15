# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        cache = {}
        def backtrack(current_sum: int=0, idx: int=0) -> int:
            if idx == len(nums):
                return 1 if current_sum == target else 0
            if (current_sum, idx) in cache:
                return cache[(current_sum, idx)]
            positive = backtrack(current_sum + nums[idx], idx + 1)
            negative = backtrack(current_sum - nums[idx], idx + 1) 
            cache[(current_sum, idx)] = positive + negative
            return cache[(current_sum, idx)]
        return backtrack()
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.findTargetSumWays([49,19,9,12,16,21,7,5,32,50,31,40,14,15,1,8,33,5,9,26], 12))