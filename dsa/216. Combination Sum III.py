# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        def backtrack(current:list[int], sum:int, used:int, num:int):
            if sum == n and used == 3:
                result.append(current)
                return
            if sum > n or num > 9 or used > k:
                return
            backtrack(current + [num], sum+num, used+1, num+1)
            backtrack(current, sum, used, num+1)
        backtrack([], 0, 0, 1)
        print
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum3(3, 7))