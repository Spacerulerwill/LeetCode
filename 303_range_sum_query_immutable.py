from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        total = 0
        for num in nums:
            total += num
            self.prefix_sum.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            left = self.prefix_sum[left - 1]
        return self.prefix_sum[right] - left
    
if __name__ == "__main__":
    obj = NumArray([1,2,3,4,5,6,7,8,9,10])
    print(obj.sumRange(10, 10))