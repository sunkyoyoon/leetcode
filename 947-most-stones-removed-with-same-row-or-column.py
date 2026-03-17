class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
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
        for i,j in stones:
            j += 1 << 31 
            union(i,j)
        ans = defaultdict(int)
        for u in p:
            ans[find(u)] += 1
        return len(stones) - len(ans)


