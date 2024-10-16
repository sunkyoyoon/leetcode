class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if max(nums) >= 2* sorted(nums)[-2]:
            return nums.index(max(nums))
        else:
            return -1
