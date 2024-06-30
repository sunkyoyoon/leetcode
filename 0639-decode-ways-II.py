class Solution:
    def numDecodings(self, s: str) -> int:
        m = 10 ** 9 + 7 
        dp = {} 
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return 1
            if s[i] == "0":
                dp[i] = 0
                return 0 

            # Initialize current dp value 
            dp[i] = 0 

            # Single character decoding 
            if s[i] == "*":
                dp[i] = 9 * dfs(i+1)
            else:
                dp[i] = dfs(i+1)

            # Two character decoding 
            if i + 1 < len(s):
                if s[i] == "*":
                    if s[i + 1] == "*":
                        dp[i] += 15 * dfs(i + 2)
                    elif '0' <= s[i + 1] <= '6':
                        dp[i] += 2 * dfs(i + 2)
                    else:
                        dp[i] += dfs(i + 2)
                elif s[i] == '1':
                    if s[i + 1] == "*":
                        dp[i] += 9 * dfs(i + 2)
                    else:
                        dp[i] += dfs(i + 2)
                elif s[i] == '2':
                    if s[i + 1] == "*":
                        dp[i] += 6 * dfs(i + 2)
                    elif '0' <= s[i + 1] <= '6':
                        dp[i] += dfs(i + 2)
                else:
                    if s[i + 1] != "*":
                        two_dig = int(s[i:i+2])
                        if 10 <= two_dig <= 26:
                            dp[i] += dfs(i + 2)
            
            dp[i] %= m
            return dp[i]

        return dfs(0)
