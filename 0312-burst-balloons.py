class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {} 
        def dp(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left + 1 == right:
                return 0 
            ans = 0 
            for i in range(left+1,right):
                total = nums[left] * nums[i] * nums[right]
                ans = max(ans, total + dp(left, i) + dp(i, right))
            memo[(left, right)] = ans
            return ans
        return dp(0, len(nums) - 1)
