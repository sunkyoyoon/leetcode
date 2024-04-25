class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv",9:"wxyz"}
        self.ans = []
        def dfs(i, curr):
            if i > len(digits) - 1:
                if curr:
                    self.ans.append(curr)
                return
            n = num[int(digits[i])]
            for c in n:
                curr += c 
                dfs(i+1, curr)
                curr = curr[0:len(curr)-1]

        dfs(0,"")
        return self.ans
