# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area = 0
        monostack = [] # monotonically increasing stack
        for i, num in enumerate(heights):
            idx = i
            # pop all heights off that are bigger, as they are the only ones that can increase
            # the the height of the histogram
            while monostack and num <= monostack[-1][0]:
                val, idx = monostack.pop()
                # compare to current max area
                max_area = max(max_area , val * (i - idx))
            # add to stack
            monostack.append((num,idx))
        # finish off any that remain at the end
        for val, idx in monostack:
            max_area = max(max_area , (len(heights) - idx) * val)
        return max_area

if __name__ == "__main__":
    solution = Solution()
    #print(solution.largestRectangleArea([2,1,5,6,2,3]))
    print(solution.largestRectangleArea([2,1,2]))
    #print(solution.largestRectangleArea([]))