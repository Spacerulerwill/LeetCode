# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        for ch1, ch2 in zip(word1, word2):
            result.append(ch1)
            result.append(ch2)
        if len(word1) > len(word2):
            result.append(word1[len(word2):len(word1)])
        elif len(word2) > len(word1):
            result.append(word2[len(word1):len(word2)])
        return "".join(result)

if __name__ == "__main__":
    solution = Solution()
    print(solution.mergeAlternately("abcaaa", "pqr"))