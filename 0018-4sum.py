class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = [] 
        def kSum(k, l, curr, target):
            if k == 2:
                r = len(nums) - 1 
                while l < r:
                    if nums[l] + nums[r] == target:
                        ans.append(curr.copy()+[nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1 
                    elif nums[l] + nums[r] > target:
                        r -= 1 
                    else:
                        l += 1
                return 
            for i in range(l,len(nums)):
                if i > l and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                kSum(k-1,i+1,curr,target-nums[i])
                curr.pop()

        kSum(4, 0, [], target)
        return ans
