# https://leetcode.com/problems/sort-an-array/description/

class MergeSort:    
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) == 1:
            return nums
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]

        self.sortArray(left)
        self.sortArray(right)

        # merge
        i = 0 # left arr index
        j = 0 # right arr index
        k = 0 # merged arr index
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
        return nums

class QuickSort:
    def sortArray(self, nums: list[int]) -> list[int]:
        ...

if __name__ == "__main__":
    merge = MergeSort()
    print(merge.sortArray([0]))
