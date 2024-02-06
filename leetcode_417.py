class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        res = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        p = set()
        a = set()
        n = len(heights)
        m = len(heights[0])

        def dfs(i, j, reachable):
            reachable.add((i, j))
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and (x, y) not in reachable and heights[x][y] >= heights[i][j]:
                    dfs(x, y, reachable)

        for i in range(n):
            dfs(i, 0, p)
            dfs(i, m - 1, a)

        for j in range(m):
            dfs(0, j, p)
            dfs(n - 1, j, a)

        for i in range(n):
            for j in range(m):
                if (i, j) in p and (i, j) in a:
                    res.append([i, j])
        
        return res
