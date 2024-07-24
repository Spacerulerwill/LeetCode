# https://leetcode.com/problems/sort-the-jumbled-numbers/

from functools import cmp_to_key

class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        nums = [(idx, num) for idx, num in enumerate(nums)]
        def comparator(x: tuple[int, int], y: tuple[int,int]) -> int:
            def map_digits(num:int) -> int:
                if num == 0:
                    return mapping[0]
                new_num = 0
                factor = 1
                while num != 0:
                    digit = num % 10
                    mapped_digit = mapping[digit]
                    new_num += mapped_digit * factor
                    factor *= 10
                    num //= 10
                return new_num
        
            if x[1] == y[1]:
                return x[0] - y[0]
            else:
                return map_digits(x[1]) - map_digits(y[1])
        return [val[1] for val in sorted(nums, key=cmp_to_key(comparator))]

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))