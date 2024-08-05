# https://leetcode.com/problems/kth-distinct-string-in-an-array/

from collections import Counter

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        counts = Counter(arr)
        i = 0
        for string, count in counts.items():
            if count == 1:
                i += 1
            if i == k:
                return string
        return ""


if __name__ == "__main__":
    solution = Solution()
    print(solution.kthDistinct(["d","b","c","b","c","a"], 2))