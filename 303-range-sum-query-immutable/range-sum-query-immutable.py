class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = None
        for x in self.nums:
            if self.prefix_sum:
                self.prefix_sum.append(self.prefix_sum[-1]+x)
            else:
                self.prefix_sum = [x]
        self.prefix_sum.append(0)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)