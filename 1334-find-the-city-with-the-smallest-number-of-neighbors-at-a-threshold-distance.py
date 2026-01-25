class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        def dijkstra(start):
            dist = [float("inf")] * n 
            dist[start] = 0 
            pq = [(0, start)]

            while pq:
                d, node = heappop(pq)
                if d > dist[node]:
                    continue 
                for nei, w in adj[node]:
                    new_dist = d + w 
                    if new_dist < dist[nei]:
                        dist[nei] = new_dist 
                        heappush(pq, (new_dist, nei))
            return sum(1 for d in dist if d <= distanceThreshold) - 1 
        
        counts = {} 
        for i in range(n):
            counts[i] = dijkstra(i)

        city = min(counts, key=lambda k: (counts[k], -k))
        return city
            

