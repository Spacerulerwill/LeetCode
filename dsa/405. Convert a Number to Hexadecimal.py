# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        result = []
        while num > 0:
            digit = num % 16
            result.append(digits[digit])
            num //= 16
        return "".join(reversed(result))


if __name__ == "__main__":
    solution = Solution()
    print(solution.toHex(26))
    print(solution.toHex(-1))