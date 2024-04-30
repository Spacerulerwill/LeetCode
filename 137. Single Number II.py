# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bit_counts = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                bit_counts[i] += num & 1
                num >>= 1
        res = 0
        bit = 1
        # first 31 bits
        for i in range(31):
            if bit_counts[i] % 3 != 0:
                res |= bit
            bit <<= 1
        # handle last sign bit seperately
        if bit_counts[31] % 3 != 0:
            res = -(2**31 - res)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.singleNumber([-2,-2,1,1,4,1,4,4,-4,-2]))