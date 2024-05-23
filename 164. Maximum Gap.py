# https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        # counting sort based on nth digit value
        def counting_sort(arr:list[int], exp:int) -> None:
            n = len(arr)
            result = [0 for _ in range(n)]
            count = [0 for _ in range(10)]
            # count digit occurence
            for i in range(n):
                count[(arr[i] // exp) % 10] += 1
            # cumulative frequency
            for i in range(1,10):
                count[i] += count[i-1]
            # sort
            for i in range(n-1, -1, -1):
                index = (arr[i] // exp) % 10
                result[count[index] - 1] = arr[i]
                count[index] -= 1
            # write to array
            for i in range(n):
                arr[i] = result[i]
        # radix sort - O(n) time and space
        def radix(arr:list[int]) -> None:
            _max = max(arr)
            exp = 1
            while _max // exp > 0:
                counting_sort(arr, exp)
                exp *= 10   
        radix(nums)
        max_gap = 0
        for i in range(1, len(nums)):
            max_gap = max(max_gap, nums[i] - nums[i-1])
        return max_gap
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumGap([3,6,9,1]))