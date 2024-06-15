# https://leetcode.com/problems/special-array-i/

class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            parity_one = nums[i] % 2
            parity_two = nums[i+1] % 2
            if parity_one == parity_two:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isArraySpecial([4,3,1,6]))