# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        num_counter = Counter(nums)
        total = 0
        for num in nums:
            complement = k - num
            if num == complement:
                if num_counter[num] >= 2:
                    total += 1
                    num_counter[num] -= 2
            else:
                if num_counter[num] > 0 and num_counter[complement] > 0:
                    total += 1
                    num_counter[num] -= 1
                    num_counter[complement] -= 1
        return total
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations([3,5,1,5], 2))