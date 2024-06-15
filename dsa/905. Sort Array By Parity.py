# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        evens = []
        odds = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        return evens + odds

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParity([3,1,2,4]))