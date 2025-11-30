class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = ""
        heap = [] 
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heappush(heap, (count, char))

        while heap:
            count, char = heappop(heap)
            if len(ans) > 1 and ans[-1] == ans[-2] == char:
                if not heap:
                    break
                count2, char2 = heappop(heap)
                ans += char2
                count2 += 1 
                if count2 < 0:
                    heappush(heap, (count2, char2))
            else:
                ans += char 
                count += 1 
            if count < 0:
                heappush(heap, (count, char))
            
        return ans
