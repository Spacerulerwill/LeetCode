# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        else:
            dp = [0,1,1] + [0 for _ in range(3, n+1)]
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[-1]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.tribonacci(4))
    print(solution.tribonacci(25))