# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        time = 0
        total_weighting_time = 0
        for customer in customers:
            arrival_time = customer[0]
            time_to_prepare = customer[1]

            if arrival_time >= time:
                time = arrival_time + time_to_prepare
                total_weighting_time += time_to_prepare
            else:
                time += time_to_prepare
                total_weighting_time += time - arrival_time
        return total_weighting_time / len(customers)


if __name__ == "__main__":
    solution = Solution()
    print(solution.averageWaitingTime([[1,2],[2,5],[4,3]]))