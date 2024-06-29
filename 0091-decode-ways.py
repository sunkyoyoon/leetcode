class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return 1 
            if i + 1 < len(s) and s[i] == "1":
                dp[i] = dfs(i+2) + dfs(i+1)
            elif i + 1 < len(s) and s[i] == "2" and s[i+1] in "0123456":
                dp[i] = dfs(i+2) + dfs(i+1)
            elif i + 1 < len(s) and s[i] == "2" and s[i+1] in "789":
                dp[i] = dfs(i+1)
            elif s[i] in "123456789":
                dp[i] = dfs(i+1)
            elif s[i] == "0":
                return 0 
            
            return dp[i]

        return dfs(0)
