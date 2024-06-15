# https://leetcode.com/problems/unique-number-of-occurrences/?envType=study-plan-v2&envId=leetcode-75

from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        number_counts = defaultdict(lambda: 0)
        for num in arr:
            number_counts[num] += 1
        seen = set()
        for count in number_counts.values():
            if count in seen:
                return False
            seen.add(count)
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniqueOccurrences([1,2,2,1,1,3]))