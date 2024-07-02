# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = []
        for num, count in counter1.items():
            if num in counter2:
                res += [num] * min(count, counter2[num])
        return res
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.intersect([1,2,2,1], [2,2]))