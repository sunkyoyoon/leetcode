class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        heap = [(0,k)]
        graph = collections.defaultdict(list)
        dist = {i:float("inf") for i in range(1,n+1)}
        for u,v,w in times:
            graph[u].append((v,w))
        
        while heap:
            weight, node = heappop(heap)
            if weight < dist[node]:
                if dist[node] != float("inf"):
                    continue
                dist[node] = weight 
            elif weight >= dist[node]:
                continue
            for v,w in graph[node]:
                heappush(heap, (w + weight, v))
        
        return max(dist.values()) if max(dist.values()) != float("inf") else -1

# O(nlogn) time
# O(n) space
