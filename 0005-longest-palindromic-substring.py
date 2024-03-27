class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = 1
        
        for j in range(len(s)):
            for i in range(j):
                if s[i] == s[j] and (i+1) <= len(s) - 1 and (j-1) >= 0 and (j - i + 1 == 2 or dp[i+1][j-1]):
                    if j - i + 1 > len(ans):
                        ans = s[i:j+1]
                    dp[i][j] = 1
        
        return ans

'''
 c   b  b  d
[[1, 0, 0, 0],  c
[0, 1, 0, 0],   b
[0, 0, 1, 0],   b
[0, 0, 0, 1]]   d
'''
