# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n in {0,1}:
            return n
        else:
            dp = [0,1] + [0 for _ in range(n-1)]
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]
            return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.fib(5))