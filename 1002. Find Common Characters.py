# https://leetcode.com/problems/find-common-characters/

from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        unique = set()
        for word in words:
            # already got all possible letters
            if len(unique) == 26:
                break
            unique = unique.union(set(word))
        counters = [Counter(word) for word in words]
        result = []
        for letter in unique:
            _min = float("inf")
            for counter in counters:
                count_of_letter = counter.get(letter, 0)
                if count_of_letter == 0:
                    _min = 0
                    break
                _min = min(_min, count_of_letter)
            result.extend([letter for _ in range(_min)])
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.commonChars(["bella","label","roller"]))