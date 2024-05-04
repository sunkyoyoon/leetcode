class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [] 
        seen = set() 
        adj = {} 
        for t in times:
            u = t[0]
            v = t[1]
            w = t[2]
            if u not in adj:
                adj[u] = []
            adj[u].append((w, v))
        
        heappush(heap, (0,k))
        while heap and len(seen) < n:
            cost, src = heappop(heap)
            seen.add(src)
            if src in adj:
                for p in adj[src]:
                    if p[1] not in seen:
                        heappush(heap, (cost + p[0], p[1]))
                        
        
        return cost if len(seen) == n else -1
