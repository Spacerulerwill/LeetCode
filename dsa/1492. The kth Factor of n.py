# https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        j = 1
        for i in range(2, n):
            if n % i == 0:
                j += 1
                if j == k:
                    return i

if __name__ == "__main__":
    solution= Solution()
    print(solution.kthFactor(12, 3))