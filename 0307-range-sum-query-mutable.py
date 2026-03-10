class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = [0] * (len(nums) + 1)
        self.nums = nums
        for i in range(len(nums)):
            val = nums[i]
            index = i + 1
            while index <= len(nums):
                self.tree[index] += val
                index += index & -index


    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index] 
        self.nums[index] = val
        index += 1 
        while index <= len(self.nums):
            self.tree[index] += diff
            index += index & -index
        
    def sumRange(self, left: int, right: int) -> int:
        total = 0 
        right += 1 
        while right > 0:
            total += self.tree[right]
            right -= right & -right
        
        while left > 0:
            total -= self.tree[left]
            left -= left & -left
        
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
