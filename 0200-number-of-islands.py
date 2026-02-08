class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen = set() 
        island = 0 

        def dfs(r,c):
            if (r,c) in seen:
                return 
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 
            if grid[r][c] == "0":
                return 
            seen.add((r,c))

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1) 


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == "1":
                    dfs(r,c)
                    island += 1 
        return island
