# https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            n = sum(int(char) * int(char) for char in str(n))

            if n == 1:
                return True
            elif n in seen:
                return False
            else:
                seen.add(n)

if __name__ == "__main__":
    solution = Solution()
    print(
        solution.isHappy(87),
        solution.isHappy(19),
        solution.isHappy(333)
    )
