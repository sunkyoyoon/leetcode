class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [[0,0]]
        seen = set()
        adj = defaultdict(list)
        ans = 0 
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                point1 = points[i]
                point2 = points[j]
                x1 = point1[0]
                x2 = point2[0]
                y1 = point1[1]
                y2 = point2[1]
                distance = abs(x1-x2) + abs(y1-y2)
                adj[i].append((distance, j))
                adj[j].append((distance, i))
        
        res = 0
        count = 0  
        while count < len(points):
            dis, index = heappop(heap)
            if index not in seen:
                res += dis
                count += 1 
                seen.add(index)
            for p in adj[index]:
                if p[1] not in seen:
                    heappush(heap, p)

        return res
