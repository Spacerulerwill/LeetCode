# https://leetcode.com/problems/ugly-number-ii

# not very fast solution, needs review!
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        two = []
        three = []
        five = []
        
        for _ in range(1,n):
            two.append(ugly_numbers[-1] * 2)
            three.append(ugly_numbers[-1] * 3)
            five.append(ugly_numbers[-1] * 5)

            _min = min(two[0], three[0], five[0])
            if two[0] == _min:
                two.pop(0)
            if three[0] == _min:
                three.pop(0)
            if five[0] == _min:
                five.pop(0)
            ugly_numbers.append(_min)
        return ugly_numbers[-1]



if __name__ == "__main__":
     solution = Solution()
     print(solution.nthUglyNumber(11))