# https://leetcode.com/problems/find-words-containing-character/

class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [idx for idx, word in enumerate(words) if x in word]

if __name__ == "__main__":
    solution = Solution()
    print(solution.findWordsContaining(["leet", "code"], "e"))
        