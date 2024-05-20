# https://leetcode.com/problems/sum-of-all-subset-xor-totals/

# Solution using backtracking to find all subsets, and applying xor reduction operation
# Time Complexity O(2^N)
class Solution1:
    def subsetXORSum(self, nums: list[int]) -> int:
        def backtrack(current:int=0, idx:int=0) -> int:
            if idx == len(nums):
                return current
            x = backtrack(current, idx + 1)
            y = backtrack(nums[idx] ^ current, idx + 1)
            return x + y
        return backtrack(0, 0)

if __name__ == "__main__":
    solution = Solution1()
    print(solution.subsetXORSum([3,4,5,6,7,8]))