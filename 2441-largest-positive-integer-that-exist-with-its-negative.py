class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for i in range(len(nums)-1,-1,-1):
            if -nums[i] in nums:
                return nums[i]
        
        return -1

