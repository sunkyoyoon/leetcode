class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        seen = {}
        def dfs(node, prev):
            if node in seen:
                return seen[node]
            seen[node] = True 
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    return True
            seen[node] = False 



        if dfs(0,None):
            return False

        return True if len(seen) == n else False
