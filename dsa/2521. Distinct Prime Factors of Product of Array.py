# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/description/

from math import sqrt

class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        prime_factors = set()
        for num in nums:
            # if divisible by 2, add to set and divide by zero as many times as possible
            if num % 2 == 0:
                prime_factors.add(2)
                while num % 2 == 0:
                    num //= 2
            # primes can only be odd now, so trial the same division technique with
            # every odd number <= sqrt(n)
            for i in range(3, int(sqrt(num)) + 1, 2):
                if num % i == 0:
                    prime_factors.add(i)
                    while num % i == 0:
                        num //= i
            # if num is still greater than 2, then its a prime as the trial division
            # was not able to reduce it to 1
            if num > 2:
                prime_factors.add(num)
        return len(prime_factors)
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.distinctPrimeFactors([2,4,3,7,10,6]))