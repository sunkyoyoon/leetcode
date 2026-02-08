class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            if dp[i] == True:
                for j in range(i,min(i+nums[i]+1, len(nums))):
                    dp[j] = True 
        
        return dp[-1]


