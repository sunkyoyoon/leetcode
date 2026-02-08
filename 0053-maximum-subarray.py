class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        ans = float("-inf")
        for n in nums:
            curr = curr + n 
            if curr > ans:
                ans = curr 
            if curr < 0:
                curr = 0 
        
        return ans


