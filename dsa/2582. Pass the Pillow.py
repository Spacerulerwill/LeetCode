# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        mod = (time % (2 * n - 2) ) + 1
        if mod > n:
            mod -= (mod - n)  * 2
        return mod

if __name__ == "__main__":
    solution = Solution()
    for i in range(16):
        print(solution.passThePillow(4, i))