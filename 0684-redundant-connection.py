class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        seen = set() 
        def dfs(u,v):
            if u == v:
                return True 
            if u in seen:
                return False 
            seen.add(u)
            for dst in graph[u]:
                if dfs(dst, v):
                    return True 
            seen.remove(u)

        for u,v in edges:
            if dfs(u,v):
                return [u,v]
            graph[u].add(v)
            graph[v].add(u)
        
