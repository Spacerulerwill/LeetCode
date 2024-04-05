# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            result <<= 1
            result |= n & 1 
            n >>= 1 
        return result 

if __name__ == "__main__":
    solution = Solution()
    print("{:032b}".format(solution.reverseBits(0b11010000000000000000000000000000)))
