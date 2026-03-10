from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        current_minimum = prices[0]
        best_profit = 0
        for price in prices[1:]:
            if price < current_minimum:
                current_minimum = price
            if price > current_minimum:
                profit = price - current_minimum
                if profit > best_profit:
                    best_profit = profit
        return best_profit


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
