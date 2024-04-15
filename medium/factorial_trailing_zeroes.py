# https://leetcode.com/problems/factorial-trailing-zeroes/description/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        # sum repeated integer division by increasing powers 5, until the result of the divison is zero
        count = 0
        divisor = 5
        while True:
            quotient = n // divisor
            if quotient == 0:
                break
            count += quotient
            divisor *= 5
        return count

if __name__ == "__main__":
    solution = Solution()
    print(solution.trailingZeroes(5))