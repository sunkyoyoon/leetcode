class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {} 
        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i >= len(s) and j >= len(p):
                return True 
            if j >= len(p):
                return False 

            if p[j] == "*":
                memo[(i,j)] = (i + 1 <= len(s) and dfs(i+1,j)) or dfs(i+1,j+1) or dfs(i,j+1)

            elif i <= len(s) - 1 and (s[i] == p[j] or p[j] == "?"):
                memo[(i,j)] = dfs(i+1,j+1)
            
            else:
                memo[(i,j)] = False

            return memo[(i,j)]

        return dfs(0,0)

