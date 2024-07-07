# https://leetcode.com/problems/guess-number-higher-or-lower/


def guess(num: int) -> int:
    ...

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = (low + high) // 2
            guess_result = guess(mid)
            if guess_result == 0:
                return mid
            elif guess_result == -1:
                high = mid - 1
            else:
                low = mid + 1
