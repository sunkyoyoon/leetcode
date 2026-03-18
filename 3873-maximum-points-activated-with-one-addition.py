class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        p = {} 
        def find(u):
            if u != p[u]:
                p[u] = find(p[u]) 
            return p[u]
        def union(u,v):
            if u not in p:
                p[u] = u 
            if v not in p:
                p[v] = v 
            p[find(u)] = find(v)
        
        for i,j in points:
            j += 1 << 31 
            union(i,j)

        count = defaultdict(int)
        
        for x,y in points:
            count[find(x)] += 1 
        vals = sorted(count.values(), reverse=True)
        return sum(vals[:2]) + 1 


            
