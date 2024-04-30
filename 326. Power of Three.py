class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 1162251467 is the largest power of 3 that can fit in a signed 32 bit integer
        # any smaller power of three therefore any smaller power of 3 will evenly divide it
        return n > 0 and 1162261467%n == 0