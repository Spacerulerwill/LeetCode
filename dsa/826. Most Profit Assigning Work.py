# https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profits: list[int], workers: list[int]) -> int:
        # sort workers and difficulty with profits rearranged so they match still - O(nlogn) quasilinear
        workers.sort()
        jobs = sorted(zip(difficulty, profits))        
        # jobs[i][0] is ith jobs difficulty
        # jobs[i][1] is ith jobs profit
        # the next part - linear
        number_jobs = len(jobs)
        total_profit = 0
        current_maximum = 0 
        i = 0
        for ability in workers:
            while i < number_jobs and ability >= jobs[i][0]:
                current_maximum = max(current_maximum, jobs[i][1])
                i += 1
            total_profit += current_maximum
        return total_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))