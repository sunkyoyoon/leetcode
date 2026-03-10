class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        def dfs(start, end):
            numOnes = s.count("1",start,end)
            if numOnes == 0:
                segCost = flatCost
            else:
                segCost = (end - start) * numOnes * encCost
            
            if (end - start) % 2 == 0:
                mid = (end + start) // 2
                splitCost = dfs(start, mid) + dfs(mid, end)
                return min(segCost, splitCost)
            
            return segCost

        return dfs(0, len(s))
