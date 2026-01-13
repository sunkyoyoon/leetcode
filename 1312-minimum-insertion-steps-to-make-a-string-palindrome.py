class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {} 
        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= j:
                return 0
            if s[i] == s[j]:
                memo[(i,j)] = dfs(i+1, j-1) 
            elif s[i] != s[j]:
                memo[(i,j)] = min(dfs(i+1, j), dfs(i, j-1)) + 1 
            return memo[(i,j)]

        return dfs(0, len(s)-1)

