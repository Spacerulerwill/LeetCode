# https://leetcode.com/problems/longest-palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_counts = {}
        for letter in s:
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
        largest_odd_count = 0
        largest_odd_letter = None
        # find largest odd numbered letter - that will be center
        for letter, count in letter_counts.items():
            if count % 2 == 1 and count > largest_odd_count:
                largest_odd_count = count
                largest_odd_letter = letter
        length = largest_odd_count
        # we have used that largest odd numbered
        if largest_odd_letter:
            letter_counts[largest_odd_letter] = 0
        # add all remaining counts rounded down to nearest 2
        for count in letter_counts.values():
            length += (count // 2) * 2
        return length

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("abccccdd"))