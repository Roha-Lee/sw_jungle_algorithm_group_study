class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]] # 중첩함수. self.grid 반복하지 않아도 되게 해줌
        :rtype: int
        """
        def dfs(grid, i, j):
            if 0<=i<m and 0<=j<n and grid[i][j] == '1':
                grid[i][j] = '2'
                dfs(grid, i+1, j)
                dfs(grid, i-1, j)
                dfs(grid, i, j+1)
                dfs(grid, i, j-1)
                
        m, n, count = len(grid), len(grid[0]), 0
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(grid, i, j)
        return count