       class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {} 

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x 
            self.rank[x] = 0 

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return False 

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootY] > self.rank[rootX]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1 
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for u,v in edges:
            uf.add(u)
            uf.add(v)

            if uf.find(u) == uf.find(v):
                return [u,v]
            uf.union(u, v)

        return 
         
