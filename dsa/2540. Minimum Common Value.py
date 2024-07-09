# https://leetcode.com/problems/minimum-common-value/description/

class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        if i == len(nums1):
            i -= 1
            while j < len(nums2):
                if nums2[j] == nums1[i]:
                    return nums1[i]
                j += 1
        else:
            j -= 1
            while i < len(nums1):
                if nums2[j] == nums1[i]:
                    return nums2[j]   
                i += 1
        return -1
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.getCommon([1,2,3], [2,4]))