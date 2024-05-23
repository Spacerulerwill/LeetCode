# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix_sums = [0 for _ in range(len(nums))]
        sum = 0
        for i in range(len(nums)):
            prefix_sums[i] = sum
            sum += nums[i]
        suffix_sums = [0 for _ in range(len(nums))]
        sum = 0
        for i in range(len(nums)-1, -1, -1):
            suffix_sums[i] = sum
            sum += nums[i]
        for idx,(a,b) in enumerate(zip(prefix_sums, suffix_sums)):
            if a == b:
                return idx
        return -1

if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex([1,7,3,6,5,6]))