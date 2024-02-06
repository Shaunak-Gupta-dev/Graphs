class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        n = len(grid)
        m = len(grid[0])
        ans = 0        
        def valid(i, j):
            return i>=0 and j>=0 and i<n and j<m
        
        def dfs(i, j):
            visited.add((i, j))
            r = 1
            for dx, dy in d:
                a, b = i+dx, j+dy
                if (valid(a, b) and grid[a][b] and (a, b) not in visited):
                    r += dfs(a, b)
            return r

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j]:
                    ans = max(ans, dfs(i, j))
        
        return ans