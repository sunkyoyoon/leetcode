class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = defaultdict(bool)

        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i > len(s)-1 and j > len(p)-1:
                return True
            if j > len(p)-1:
                return False

            if i <= len(s)-1 and s[i] == p[j]:
                memo[(i,j)] = memo[(i,j)] or dfs(i+1,j+1)
            if p[j] == "." and (j+1) <= len(p)-1 and p[j+1] == "*":
                if i <= len(s) - 1:
                    memo[(i,j)] = memo[(i,j)] or dfs(i+1,j) or dfs(i+1,j+2)
                else:
                    memo[(i,j)] = memo[(i,j)] or df
