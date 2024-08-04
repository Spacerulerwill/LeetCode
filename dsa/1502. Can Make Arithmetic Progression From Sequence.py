# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        if len(arr) <= 1:
            return True
        arr.sort()
        last_diff = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i-1] != last_diff:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canMakeArithmeticProgression([1,5,3]))
    print(solution.canMakeArithmeticProgression([1,2,4]))