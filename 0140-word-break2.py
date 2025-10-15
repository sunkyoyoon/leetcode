class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def dfs(i, res):
            if i > len(s) - 1:
                ans.append(" ".join(res))
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    res.append(s[i:j+1])
                    dfs(j+1,res)
                    res.pop()

        dfs(0, [])
        return ans
