class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {} 
        def dfs(alice, m, index):
            if index == len(piles):
                return 0
            if (alice, m, index) in dp:
                return dp[(alice, m, index)]
            total = 0 
            res = 0 if alice else float("inf")
            for x in range(1, 2 * m + 1):
                if index + x > len(piles):
                    break
                
                total += piles[index + x - 1]
                if alice:
                    res = max(res, total + dfs(not alice, max(x, m), x + index))
                else:
                    res = min(res, dfs(not alice, max(x, m), x + index))
            dp[(alice, m, index)] = res
            return res 
        return dfs(True, 1, 0)
        
    # O(N^2) time 
    # O(N^2) space
