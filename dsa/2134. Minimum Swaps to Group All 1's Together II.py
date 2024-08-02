# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        ones = sum(1 for num in nums if num == 1)
        i = 0
        j = ones - 1
        # amount of ones in initial windows
        current_ones = 0
        for k in range(ones):
            current_ones += int(nums[k] == 1)
        minSwaps = ones - current_ones
        for _ in range(n-1):
            if nums[i] == 1:
                current_ones -= 1
            i = (i + 1) % n
            j = (j + 1) % n
            if nums[j] == 1:
                current_ones += 1
            minSwaps = min(minSwaps, ones - current_ones)
        return minSwaps

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSwaps([0,1,0,1,1,0,0]))