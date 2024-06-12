# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1
            if c_bit == 0:
                if a_bit == 1:
                    flips += 1
                if b_bit == 1:
                    flips += 1
            else:
                if a_bit == 0 and b_bit == 0:
                    flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips

if __name__ == "__main__":
    solution = Solution()
    print(solution.minFlips(2, 6, 5))