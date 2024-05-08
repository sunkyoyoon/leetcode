class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        hashmap = {char: [] for word in words for char in word}
        for i in range(len(words)):
            if i > 0:
                first = words[i-1]
                second = words[i]
                minLen = min(len(first), len(second))
                if len(first) > len(second) and first[:minLen] == second[:minLen]:
                    return ""
                for j in range(minLen):
                    if first[j] != second[j]:
                        hashmap[first[j]].append(second[j])
                        break

        seen = {}
        res = []

        def dfs(c):
            if c in seen:
                return seen[c]
            seen[c] = True
            for ch in hashmap[c]:
                if dfs(ch):
                    return True
            seen[c] = False
            res.append(c)

        for c in hashmap:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
