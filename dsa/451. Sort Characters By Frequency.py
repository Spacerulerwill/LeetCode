# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(char * count for char, count in Counter(s).most_common())

if __name__ == "__main__":
    solution = Solution()
    print(solution.frequencySort("tree"))
    print(solution.frequencySort("cccaaa"))
    print(solution.frequencySort("Aabb"))
    print(solution.frequencySort("loveleetcode"))