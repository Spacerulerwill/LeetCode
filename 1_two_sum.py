from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [idx, seen[complement]]
            else:
                seen[num] = idx
