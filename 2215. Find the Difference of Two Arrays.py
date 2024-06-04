# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result1 = [num for num in nums1 if num not in nums2]
        result2 = [num for num in nums2 if num not in nums1]
        return [result1, result2]
 
if __name__ == "__main__":
    solution = Solution()
    print(solution.findDifference([1,2,3], [2,4,6]))