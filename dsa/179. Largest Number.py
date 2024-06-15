from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def custom_sort_key(a:str, b:str) -> int:
            if a + b > b + a:
                return 1
            elif a + b < b + a:
                return -1
            else:
                return 0
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(custom_sort_key), reverse=True)
        result = "".join(nums)
        if all(char == "0" for char in result):
            return "0"
        else:
            return result.lstrip("0")

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestNumber([0,0]))