# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        print(candidates)
        res = []
        def backtrack(current:list=[], sum:int = 0, idx:int=0):
            if sum == target:
                res.append(current)
                return    
            if sum > target:
                return
            for i in range(idx, len(candidates)):
                # Skip duplicates
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(current + [candidates[i]], sum + candidates[i], i + 1)
        backtrack()
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum2([1, 1, 2, 5, 6, 7, 10], 8))