# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numFull = numBottles
        numEmpty = 0
        total = 0
        while True:
            total += numFull
            numEmpty += numFull
            numFull = 0

            if numEmpty < numExchange:
                break

            exchanged = numEmpty // numExchange
            numFull += exchanged
            numEmpty -= (exchanged * numExchange)
        return total

if __name__ == "__main__":
    solution = Solution()
    print(solution.numWaterBottles(15, 4))