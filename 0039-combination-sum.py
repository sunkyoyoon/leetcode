class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, curr):
            if sum(curr) == target:
                ans.append(curr.copy())
                return
            if sum(curr) > target:
                return 
            for j in range(i,len(candidates)):
                curr.append(candidates[j])
                backtrack(j, curr)
                curr.pop() 

        backtrack(0, [])
        return ans
