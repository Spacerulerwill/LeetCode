# https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution:
    def sampleStats(self, count: list[int]) -> list[float]:
        element_sum = sum(count)
        def get_min() -> float:
            _min = 0
            while _min < len(count) and count[_min] == 0:
                _min += 1
            return float(_min)
        # get maximum by finding index of last non zero element
        def get_max() -> float:
            _max = len(count) - 1
            while _max > 0 and count[_max] == 0:
                _max -= 1
            return float(_max)
        # mean
        def get_mean() -> float:
            return (sum(i * val for i, val in enumerate(count))) / element_sum
        # median is half way element
        def kth(k) -> float:
            for elem, cnt in enumerate(count):
                k -= cnt
                if k <= 0:
                    return elem
        def get_median() -> float:
            if element_sum & 1 == 1:
                return kth(element_sum // 2 + 1)
            else:
                return (kth(element_sum // 2) + kth(element_sum // 2 + 1)) / 2
        # mode is index of element with max czunt
        def get_mode() -> float:
            mode = 0
            max_count = 0
            for num, c in enumerate(count):
                if c > max_count:
                    max_count = c
                    mode = num
            return float(mode)

        return [get_min(), get_max(), get_mean(), get_median(), get_mode()]

if __name__ == "__main__":
    solution = Solution()
    print(solution.sampleStats([0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))