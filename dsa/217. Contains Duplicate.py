# https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsDuplicate([1,2,3,1]))
    print(solution.containsDuplicate([1,2,3,4]))
    print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))