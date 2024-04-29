# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        for idx, temperature in enumerate(temperatures):
            while len(stack) > 0 and temperature > stack[-1][1]:
                stack_idx, _ = stack.pop()
                result[stack_idx] = idx - stack_idx
            stack.append((idx, temperature))
        return result
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))

