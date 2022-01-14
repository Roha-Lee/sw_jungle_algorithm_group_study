class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        sys.setrecursionlimit(10**8)
        def dfs(x, y):
            if x < 0 or x >= col_len or y < 0 or y >= row_len:
                return
            
            if grid[x][y] == '0':
                return
            
            # if grid[x][y] == '1':
            #     checklist[x][y] = True
            grid[x][y] = 0
            
            for i in range(4):
                dfs(x + dx[i], y + dy[i])
            
            
        col_len = len(grid)
        row_len = len(grid[0])
        
        # checklist = [[False] * row_len for _ in range(col_len)]
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        
        cnt = 0
        
        for i in range(col_len):
            for j in range(row_len):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt += 1
        
        return cnt
        