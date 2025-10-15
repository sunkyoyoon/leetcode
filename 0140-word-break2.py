class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]
            if i in memo:
                return memo[i]
            res = [] 
            for j in range(i,len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    subs = dfs(j+1)
                    for sub in subs:
                        if sub:
                            res.append(word + " " + sub)
                        else:
                            res.append(word)
                    
            memo[i] = res 
            return memo[i]

        return dfs(0)
