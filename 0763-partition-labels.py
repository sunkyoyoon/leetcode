class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ans = [] 
        letters = Counter(s)

        temp = [] 
        left = 0 
        for i in range(len(s)):
            c = s[i]
            letters[c] -= 1 
            if c in temp and letters[c] == 0:
                temp.remove(c)
            elif c not in temp and letters[c] > 0:
                temp.append(c)
            if temp == []:
                ans.append(i+1 - left)
                left = i + 1
        return ans
            
