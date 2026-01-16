class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        heap = [(0,1)]
        graph = collections.defaultdict(list)
        ans = [] 

        best = [float("inf")] * (n + 1)
        second = [float("inf")] * (n + 1)
        best[1] = 0

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        while heap:
            weight, node = heappop(heap)

            if weight > second[node]:
                continue 

            if node == n and weight == second[n]:
                return weight 

            t = weight 
            if (t // change) % 2 == 1:
                t = (t // change + 1) * change

            for nei in graph[node]:
                next_time = t + time 
                if next_time < best[nei]:
                    second[nei] = best[nei]
                    best[nei] = next_time
                    heappush(heap, (next_time, nei))

                elif best[nei] < next_time < second[nei]:
                    second[nei] = next_time
                    heappush(heap, (next_time, nei))

# O((V+E)logV) time
# O(V+E) space 
