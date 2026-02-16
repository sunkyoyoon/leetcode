from typing import (
    List,   
)
from lintcode import (
    Point,
)

"""
Definition for a point:
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
"""
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.count = 0

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x 
            self.rank[x] = 0
            self.count += 1 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False 

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1 
        self.count -= 1 
        return True 
        

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def num_islands2(self, n: int, m: int, operators: List[Point]) -> List[int]:
        uf = UnionFind()
        grid = set()
        result = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for point in operators:
            r, c = point.x, point.y
            if (r, c) in grid:
                result.append(uf.count)
                continue

            grid.add((r, c))
            uf.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in grid:
                    uf.union((r, c), (nr, nc))

            result.append(uf.count)

        return result

