# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(subset:list, idx:int):
            if idx == len(nums):
                res.append(subset)
                return
            backtrack(subset, idx+1)
            backtrack(subset+[nums[idx]], idx+1)
        backtrack([], 0)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3]))

1,2,3