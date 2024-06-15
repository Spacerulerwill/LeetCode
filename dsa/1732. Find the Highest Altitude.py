# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sums = [0 for _ in range(len(gain)+1)]
        sum = 0
        for i in range(len(gain)):
            prefix_sums[i] = sum
            sum += gain[i]
        # last one
        prefix_sums[-1] = (prefix_sums[-2] + gain[-1])
        return max(prefix_sums)

if __name__ == "__main__":
    solution = Solution()
    print(solution.largestAltitude([44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]))