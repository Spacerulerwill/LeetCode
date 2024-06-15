# https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        counts = {num: 0 for num in arr2}
        for num in arr1:
            if num in counts:
                counts[num] += 1
        result = []
        for num, count in counts.items():
            result.extend([num for _ in range(count)])
        arr2 = set(arr2)
        arr1 = [num for num in arr1 if num not in arr2]
        result.extend(sorted(arr1))
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))
