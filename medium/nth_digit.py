# https://leetcode.com/problems/nth-digit/
from math import ceil

class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        digit_sum = 0
        while True:
            sum = (9 * (10**(i-1)) * i)
            if digit_sum + sum >= n:
                i -= 1
                break
            else:
                digit_sum += sum
                i += 1
        digits_remaining = n - digit_sum
        number_in = (10**i) + ceil(digits_remaining / (i+1)) - 1
        digit_idx = (digits_remaining-1) % (i+1)
        return (number_in // 10**(i-digit_idx)) % 10
        
if __name__ == "__main__":
    solution = Solution()    
    print(solution.findNthDigit(3))
    print(solution.findNthDigit(11))
