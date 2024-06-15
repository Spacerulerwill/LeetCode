# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numset = set(nums)
        max_consecutive = 0
        for num in nums:
            if num - 1 not in numset:
                i = 1
                while num + i in numset:
                    i += 1
                max_consecutive = max(max_consecutive, i)
        return max_consecutive

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))