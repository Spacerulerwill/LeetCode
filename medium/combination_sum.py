# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def backtrack(current:list=[], sum:int = 0, idx:int = 0):
            if sum == target:
                res.append(current)
                return
            
            if idx == len(candidates) or sum > target:
                return
            
            backtrack(current + [candidates[idx]], sum + candidates[idx], idx)
            backtrack(current, sum, idx + 1)
        backtrack()
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2,3,6,7], 7))