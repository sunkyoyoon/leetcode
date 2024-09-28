class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2 or len(nums) == 3:
            return max(nums)

        t1 = nums[len(nums) - 2]
        t2 = nums[len(nums) - 1]
        ans = 0 
        for i in range(len(nums)-3):
            ans = max(nums[i] + t1, t2)
            if t1 < t2:
                t1 = t2
            t2 = ans
        
        ans2 = 0 
        t1 = 0 
        t2 = nums[len(nums)-1]
        for i in range(len(nums)-2):
            ans2 = max(nums[i] + t1, t2)
            t1 = t2 
            t2 = ans2 

        return max(ans, ans2)
