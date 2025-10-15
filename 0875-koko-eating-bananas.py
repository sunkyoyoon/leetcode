class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            res = 0  
            for n in piles:
                res += math.ceil(n / m)
            if res > h:
                l = m + 1
            else:
                r = m
        
        return l 
