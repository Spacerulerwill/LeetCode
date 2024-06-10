# https://leetcode.com/problems/height-checker/description/?envType=daily-question&envId=2024-06-10

# using counting sort by finding min and max, optimal memory counting sort
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        min_height = min(heights)
        max_height = max(heights)
        counts = [0 for _ in range(max_height - min_height + 1)]
        for height in heights:
            counts[height-min_height] += 1
        expected_heights = [0 for _ in range(len(heights))]
        i = 0
        for idx, count in enumerate(counts):
            for _ in range(count):
                expected_heights[i] = min_height + idx
                i += 1
        result = 0
        for height, expected in zip(heights, expected_heights):
            if height != expected:
                result += 1
        return result
 
if __name__ == "__main__":
    solution = Solution()
    print(solution.heightChecker([1,1,4,2,1,3]))