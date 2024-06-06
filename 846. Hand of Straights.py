# https://leetcode.com/problems/hand-of-straights/

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # no elements or group size of 1 always possible
        if len(hand) == 0 or groupSize == 1:
            return True
        # if we cant evenly split into groups
        if len(hand) % groupSize != 0:
            return False
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))