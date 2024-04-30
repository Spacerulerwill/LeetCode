# https://leetcode.com/problems/first-missing-positive/


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        smallest = 1
        seen = set()
        for num in nums:
            if num < smallest:
                continue
            if num == smallest:
                while True:
                    smallest += 1
                    if smallest not in seen:
                        break
            else:
                seen.add(num)
        return smallest
"""
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 1            
        new = sorted([num for num in nums if num > 0])
        if len(new) == 0:
            return 1
        if new[0] != 1:
            return 1
        else:
            for i in range(len(new) - 1):
                if new[i+1] - new[i] > 1:
                    return new[i] + 1
            return new[-1] + 1
"""
                
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([1, 1000]))