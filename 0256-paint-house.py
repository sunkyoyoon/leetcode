class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        nums = costs
        memo = {} 
        def helper(i, j):
            if i < 0:
                return 0 
            if (i,j) in memo:
                return memo[(i,j)]
            if j == 0:
                memo[(i,j)] = nums[i][j] + min(helper(i-1, 1), helper(i-1, 2))
            if j == 1:
                memo[(i,j)] = nums[i][j] + min(helper(i-1, 0), helper(i-1, 2))
            if j == 2:
                memo[(i,j)] = nums[i][j] + min(helper(i-1, 0), helper(i-1, 1))
            return memo[(i,j)]
        
        return min(helper(len(nums)-1,0), helper(len(nums)-1,1), helper(len(nums)-1,2))
