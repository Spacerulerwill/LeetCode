# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int=0):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start] 
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start] 
                
        res = []
        backtrack()
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.permute([1,2,3]))