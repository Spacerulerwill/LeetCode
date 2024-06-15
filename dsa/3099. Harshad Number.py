# https://leetcode.com/problems/harshad-number/

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        total = 0
        temp = x
        while temp != 0:
            total += temp % 10
            temp //= 10
        return total if x % total == 0 else -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfTheDigitsOfHarshadNumber(18))
    print(solution.sumOfTheDigitsOfHarshadNumber(23))