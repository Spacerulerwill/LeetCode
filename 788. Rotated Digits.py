# https://leetcode.com/problems/rotated-digits/

class Solution:
    def rotatedDigits(self, n: int) -> int:
        num_good = 0
        for i in range(1, n+1):
            has_unrotatable_digit = False
            has_rotatable_digit = False
            while i:
                digit = i % 10
                # if it contains a 3,4,7 it cannot be a good number, as they cant be rotated
                if digit in {3,4,7}:
                    has_unrotatable_digit = True
                    break
                elif digit in {2,5,6,9}:
                    has_rotatable_digit = True
                i //= 10
            num_good += int(not has_unrotatable_digit and has_rotatable_digit)
        return num_good

if __name__ == "__main__":
    solution = Solution()
    print(solution.rotatedDigits(10))
    print(solution.rotatedDigits(1))    
    print(solution.rotatedDigits(2))
    print(solution.rotatedDigits(847))    
