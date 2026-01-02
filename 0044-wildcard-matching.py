class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {} 
        if s and p and s[-1] != p[-1] and p[-1] != "*" and p[-1] != "?":
            return False
        def dfs(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == len(s) and j == len(p):
                return True 
            elif i == len(s) and j < len(p):
                while j < len(p) and p[j] == "*":
                    j += 1 
                if j == len(p):
                    return True 
                else:
                    return False
            elif i < len(s) and j == len(p):
                return False
            
            if s[i] == p[j] or p[j] == "?":
                memo[(i,j)] = dfs(i+1, j+1)
            elif p[j] == "*":
                memo[(i,j)] = dfs(i, j+1) or dfs(i+1, j)
            else:
                memo[(i,j)] = False
            return memo[(i,j)]
                

        return dfs(0,0)
