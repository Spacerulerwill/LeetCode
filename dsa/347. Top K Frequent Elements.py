# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == k:
            return nums
        
        # determine element frequencies
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

        # put into buckets, where bucket[i] stores the amount of elements with frequency (i+1)
        buckets = [[] for _ in range(len(nums))]
        for element, frequency in counts.items():
            buckets[frequency - 1].append(element)
        
        answer = []
        for bucket in reversed(buckets):
            for elem in bucket:
                answer.append(elem)
                if len(answer) == k:
                    return answer

if __name__ == "__main__":
    solution = Solution()
    #print(solution.topKFrequent([1,1,1,2,2,3], 2))
    #print(solution.topKFrequent([1], 1))
    print(solution.topKFrequent([4,1,-1,2,-1,2,3], 2))