class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        ans = float("inf")
        for i in range(len(nums)):
            l = i + 1 
            r = len(nums) - 1
            while l < r:
                summed = nums[i] + nums[l] + nums[r]
                if abs(summed - target) < abs(ans - target):
                    ans = summed 
                   
                if summed > target:
                    r -= 1 
                if summed < target:
                    l += 1 
                if summed == target:
                    return target
        return ans
