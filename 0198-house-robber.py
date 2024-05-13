class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} 
        def helper(i):
            if i < 0:
                return 0 
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + helper(i-2), helper(i-1))
            return memo[i]
        
        return helper(len(nums)-1)
