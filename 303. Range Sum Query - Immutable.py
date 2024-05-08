class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix_sums = [0]
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            self.prefix_sums.append(prefix_sum)
        
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sums[right+1] - self.prefix_sums[left]
        
if __name__ == "__main__":
    obj = NumArray([1,2,3,4,5,6,7,8,9,10])
    print(obj.sumRange(0, 3))