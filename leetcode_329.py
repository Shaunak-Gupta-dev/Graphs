class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        n = len(matrix)
        m = len(matrix[0])
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        ans = 0

        def valid(i, j):
            return i>=0 and j>=0 and i<n and j<m

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            r = 1

            for dx, dy in d:
                a = i+dx
                b = j+dy
                if valid(a, b) and matrix[a][b] > matrix[i][j]:
                    r = max(r, 1+dfs(a, b))

            cache[(i, j)] = r
            return cache[(i, j)]

        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))
        
        return ans

        