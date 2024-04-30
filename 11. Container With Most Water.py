# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        _max = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            _max = max(_max, current_height * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return _max

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([2,3,4,5,18,17,6]))
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
