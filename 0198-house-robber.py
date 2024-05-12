class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        for i in range(len(nums)):
            if i == 2:
                nums[i] = nums[i] + nums[i-2]
            if i > 2:
                nums[i] = nums[i] + max(nums[i-2], nums[i-3])
        
        return max(nums[len(nums)-2], nums[len(nums)-1])
