class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = [] 
        def backtrack(k, curr, left, target):
            if k == 2:
                right = len(nums) - 1 
                while left < right:
                    if nums[left] + nums[right] == target:
                        ans.append(curr + [nums[left], nums[right]])
                        left += 1 
                        right -= 1 
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1 

                    elif nums[left] + nums[right] > target:
                        right -= 1 
                    else:
                        left += 1 
                return 
            for i in range(left,len(nums)):
                if i > left and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                backtrack(k-1, curr, i + 1, target - nums[i])
                curr.pop()

        backtrack(4, [], 0, target)
        return ans
