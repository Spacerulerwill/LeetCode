# https://leetcode.com/problems/sort-the-jumbled-numbers/

from functools import cmp_to_key

class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        def map_digits(num: int) -> int:
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
        
        mapped_nums = {num: map_digits(num) for num in nums}
        nums.sort(key=lambda num: mapped_nums[num])
        return nums

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]))