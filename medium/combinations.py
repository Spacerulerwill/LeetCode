# https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def backtrack(combination: list[int], start: int):
            if len(combination) == k:
                res.append(combination[:])
                return
            if len(combination) + (n - start + 1) < k:
                return
            for i in range(start, n + 1):
                backtrack(combination + [i], i + 1)        
        backtrack([], 1)
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(4, 2))