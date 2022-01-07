class Solution:
    def dfs(self, grid, r, c):
        rows, cols = len(grid), len(grid[0])
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    self.dfs(grid, nr, nc)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        num = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    self.dfs(grid, r, c)
                    num += 1
        return num
                