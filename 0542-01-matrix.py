class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()

        grid = [[float("inf")] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    grid[r][c] = 0
                    q.append((r, c))
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] > grid[r][c] + 1:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr, nc))
        
        return grid

