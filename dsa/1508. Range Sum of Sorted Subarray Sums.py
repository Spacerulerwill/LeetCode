# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/

class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        sum_of_subarrays = []
        for i in range(n):
            _sum = 0
            for j in range(i, n):
                _sum += nums[j]
                sum_of_subarrays.append(_sum)
        sum_of_subarrays.sort()
        return sum(sum_of_subarrays[left-1:right]) % 1e9

if __name__ == "__main__":
    solution = Solution()
    print(solution.rangeSum([1,2,3,4], 4, 1, 5))