class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0 
        for i in range(len(nums)):
            n = nums[i]
            for j in range(i, i + n + 1):
                if j == len(nums):
                    break
                dp[j] = min(dp[j], 1 + dp[i])
        
        return dp[-1]

