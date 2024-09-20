class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        ans = float("inf")
        index1 = None
        index2 = None
        for i in range(len(wordsDict)):
            word = wordsDict[i]

            if word == word1:
                index1 = i 
                if index2 != None:
                    ans = min(ans, index1 - index2)
            elif word == word2:
                index2 = i 
                if index1 != None:
                    ans = min(ans, index2 - index1)
            print(index1, index2)
        return ans if ans != float("inf") else 0
