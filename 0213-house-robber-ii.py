class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        left = 0 
        right = 0 
        for i in range(len(nums)):
            nums[i] = max(nums[i] + left, right)
            left = right 
            right = nums[i]
        return nums[-1]
