class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = []
        total = 0 
        for p, u, v in trips:
            events.append((u,p))
            events.append((v,-p))

        events.sort()
        for _,p in events:
            total += p 
            if total > capacity:
                return False
        return True


