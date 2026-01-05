class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        for u, v in edges:
            stack = [u]
            seen = set()

            while stack:
                src = stack.pop()
                if src == v:
                    return [u, v]

                if src in seen:
                    continue
                seen.add(src)

                for dst in graph[src]:
                    if dst not in seen:
                        stack.append(dst)

            graph[u].add(v)
            graph[v].add(u)
