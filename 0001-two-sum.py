class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i in range(len(nums)):
            num = target - nums[i]
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[nums[i]] = i 
        

