# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # extract odd bits (1 indexed)
        k = n & 0b01010101010101010101010101010101
        # extract even bits (1 indexed)
        j = n & 0b10101010101010101010101010101010
        # check 3 things:
        # * k has more than 0 bits set
        # * k is a power of 2 (only 1 bit set)
        # * there are no bits set in j
        return k > 0 and (k & (k-1)) == 0 and j == 0
    
if __name__ == "__main__":
    solution = Solution()
    for i in range(1, 65):
        print(f"{i}: {solution.isPowerOfFour(i)}")