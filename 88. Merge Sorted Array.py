# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        finalIdx = m + n - 1
        idx1 = m - 1
        idx2 = n - 1
        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[finalIdx] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[finalIdx] = nums2[idx2]
                idx2 -= 1
            finalIdx -= 1

        if idx1 >- 0:
            while finalIdx >= 0:
                nums1[finalIdx] = nums1[idx1]
                idx1 -= 1
                finalIdx -= 1

        if idx2 >= 0:
            while finalIdx >= 0:
                nums1[finalIdx] = nums2[idx2]
                idx2 -= 1
                finalIdx -= 1
                


if __name__ == "__main__":
    solution = Solution()
    array1 = [1,2,3,0,0,0]
    array2 = [2,5,6]
    solution.merge(array1, 3, array2, 3)
    print(array1)
        