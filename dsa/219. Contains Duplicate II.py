# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = idx
            else:
                if idx - seen[num] <= k:
                    return True
                else:
                    seen[num] = idx
        return False

if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1,2,3,1]))