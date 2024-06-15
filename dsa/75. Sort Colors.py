# https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for num in nums:
            counts[num] += 1
        idx = 0
        for i in range(len(counts)):
            for _ in range(counts[i]):
                nums[idx] = i
                idx += 1

if __name__ == "__main__":
    solution = Solution()
    nums = [2,0,2,1,1,0]
    solution.sortColors(nums)
    print(nums)