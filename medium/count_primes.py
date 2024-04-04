# https://leetcode.com/problems/count-primes/

from math import sqrt, ceil

class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [False, False] + [True for _ in range(2, n)]
        for p in range(2, int(ceil(sqrt(n)))):
            if (prime[p]):
                for i in range(p*p, n, p):
                    prime[i] = False
        return sum(1 for value in prime if value)

if __name__ == "__main__":
    solution = Solution()
    print(solution.countPrimes(12))