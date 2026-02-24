class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        i = 1
        for _ in range(32):
            if n & i != 0:
                count += 1
            i <<= 1
        return count
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.hammingWeight(5))