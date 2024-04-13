# https://leetcode.com/problems/shifting-letters/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        result = ""
        shift_sum = sum(shifts)
        for char, shift_sub in zip(s, shifts):
            result += chr(97 + (ord(char) - 97 + shift_sum) % 26)
            shift_sum -= shift_sub
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.shiftingLetters("abc", [3,5,9]))
    print(solution.shiftingLetters("aaa", [1,2,3]))