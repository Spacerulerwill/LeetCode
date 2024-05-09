class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        turns = 0
        for i in range(k):
            val = happiness[i] - turns
            if val <= 0:
                break
            total += val
            turns += 1
        return total
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumHappinessSum([12,1,42], 3))