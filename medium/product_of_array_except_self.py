# https://leetcode.com/problems/product-of-array-except-self/

from operator import mul

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # prefix products
        prefix_products = [1]
        total = 1
        for i in range(1, len(nums)):
            total *= nums[i-1]
            prefix_products.append(total)
        # suffix products
        suffix_products = [1]
        total = 1
        for i in range(len(nums)-1, 0, -1):
            total *= nums[i]
            suffix_products.append(total)
        return list(map(mul, prefix_products, reversed(suffix_products)))


if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf([1,2,3,4]))