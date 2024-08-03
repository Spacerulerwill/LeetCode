# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

from collections import Counter

class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        return Counter(target) == Counter(arr)

if __name__ == "__main__":
    solution = Solution()
    print(solution.canBeEqual([1,2,3,4], [2,4,1,3]))