class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        seen = set() 
        ans = 0 

        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        def dfs(node):
            if node in seen:
                return 
            seen.add(node)
            for nei in adj[node]:
                dfs(nei)


        
        for i in range(n):
            if i not in seen:
                ans += 1 
                dfs(i)
        return ans
