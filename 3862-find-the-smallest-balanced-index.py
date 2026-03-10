class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        left = sum(nums)

        right = 1 

        for i in range(len(nums)-1,-1,-1):
            left -= nums[i]
            if left == right:
                return i 
            right *= nums[i]
        return -1
