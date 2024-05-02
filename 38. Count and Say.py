# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        previous = "1"
        # calculate rle of previous
        for _ in range(1, n):
            new = ""
            count = 0
            cur = previous[0]
            i = 0
            while True:
                if previous[i] == cur:
                    count += 1
                else:
                    new += str(count)
                    new += cur
                    cur = previous[i]
                    count = 1
                if i == len(previous)-1:
                    new += str(count)
                    new += cur
                    break
                i += 1
            previous = new
        return previous

if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(4))