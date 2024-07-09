# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        previous_ones = 0
        current_ones = 0
        _max = 0
        has_zero = False
        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                _max = max(_max, current_ones + previous_ones)
                previous_ones = current_ones
                current_ones = 0
                has_zero = True
        _max = max(_max, current_ones + previous_ones)
        if not has_zero:
            return len(nums)-1
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestSubarray([0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1]))