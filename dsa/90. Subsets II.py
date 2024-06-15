# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        def backtrack(subset:list=[], idx:int=0):
            res.append(subset)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue 
                backtrack(subset + [nums[i]], i + 1)
        backtrack()
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsetsWithDup([1,2,2]))