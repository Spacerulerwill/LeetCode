# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word)
        counter = [(letter, count) for letter, count in counter.items()]
        counter.sort(key=lambda item: item[1], reverse=True)
        word = []
        for letter, count in counter:
            word.extend([letter] * count)
        prev_char = word[0]
        letter_costs = {prev_char: 1}
        current_cost = 1
        current_number = 2
        total_cost = 1
        for i in range(1, len(word)):
            prev_char = word[i-1]
            current_char = word[i]
            if current_char != prev_char:
                if current_number == 9:
                    current_number = 2
                    current_cost += 1
                else:
                    current_number += 1
            total_cost += current_cost
        return total_cost

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumPushes("aabbccddeeffgghhiiiiii"))
    print(solution.minimumPushes("xyzxyzxyzxyz"))