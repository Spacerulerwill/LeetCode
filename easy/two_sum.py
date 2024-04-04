# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [idx, seen[complement]]
            else:
                seen[num] = idx

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9)) 