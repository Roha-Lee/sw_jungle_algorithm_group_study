# LeetCode 200. Number of Island
# https://leetcode.com/problems/number-of-islands/

# 섬의 갯수를 세는 문제 (DFS)

# Runtime : 415ms(76.39%)
# Memory Usage : 16.9MB (6.67%)

class Solution:            
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        for y in range(len(grid)):              # len(grid) -> grid의 원소 갯수 4 출력  0~3
            for x in range(len(grid[0])):       # 여기서 len(grid[0])면 5가 출력 0~4
                if grid[y][x] == '1':           # grid[y][x]의 값이 1일 경우 answer 1씩 가산 
                    self.count(y,x,grid)        # 그 후 상하좌우 1값지우는 재귀함수
                    answer +=1
                    
        return answer
    
    def count(self, y, x, grid):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] != '1':
            return
        grid[y][x] = '#'
        self.count(y+1,x,grid)  # 상
        self.count(y-1,x,grid)  # 하
        self.count(y,x-1,grid)  # 좌
        self.count(y,x+1,grid)  # 우