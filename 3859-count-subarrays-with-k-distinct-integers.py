class Solution:
    def countSubarrays(self, nums: list[int], k: int, m: int) -> int:
        countd = defaultdict(int)
        countv = defaultdict(int)
        leftd = 0 
        leftv = 0
        vcount = 0 
        res = 0  

        for right, curr in enumerate(nums):
            countd[curr] += 1
            while len(countd) > k:
                countd[nums[leftd]] -= 1
                if countd[nums[leftd]] == 0:
                    del countd[nums[leftd]]
                leftd += 1 
            
            countv[curr] += 1 
            if countv[curr] == m:
                vcount += 1 
            while vcount >= k:
                if countv[nums[leftv]] == m:
                    vcount -= 1
                countv[nums[leftv]] -= 1 
                leftv += 1 

            if leftv > leftd:
                res += leftv - leftd
        return res

