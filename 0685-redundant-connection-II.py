class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent_of = [0] * (n+1)
        cand1 = None
        cand2 = None
        for u,v in edges:
            if parent_of[v] != 0:
                cand1 = [parent_of[v], v]
                cand2 = [u, v]
            else:
                parent_of[v] = u 

        parent = list(range(n + 1))
        # [0,1,2,3,4,5]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        for u,v in edges:
            if cand2 and [u,v] == cand2:
                continue
            du = find(u)
            dv = find(v)
            #cycle found
            if du == dv:
                if cand1:
                    return cand1
                else:
                    return [u,v]
            

            parent[dv] = du 
        
        return cand2
