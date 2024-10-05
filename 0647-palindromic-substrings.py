class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ans = 0 

        def checker(i):
            j = 1     
            ans = 0      
            while i - j >= 0 and i + 1 + j < len(s):
                if dp[i-j+1][i+j] and s[i-j] == s[i+1+j]:
                    dp[i-j][i+1+j] = True 
                    ans += 1 
                j += 1 
            return ans

        for i in range(len(s)):
            dp[i][i] = True 
            if i + 1 < len(s):
                if s[i] == s[i+1]:
                    dp[i][i+1] = True
                    ans += 1 
                    ans += checker(i)
            ans += 1  
            j = 1  
            while i - j >= 0 and i + j < len(s):
                if dp[i-j+1][i+j-1] and s[i-j] == s[i+j]:
                    dp[i-j][i+j] = True 
                    ans += 1 
                j += 1 

        return ans
    
