class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs)
        ans = ""
        j = 0 
        for i in range(len(min_str)):
            letter = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != letter:
                    return ans 
            ans += letter
        
        return ans 

# O(N) time
# O(1) space
