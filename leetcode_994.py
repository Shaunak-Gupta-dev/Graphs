class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        d = [[0,1], [1,0], [0,-1], [-1,0]]
        q = deque()

        def valid(i, j):
            return i>=0 and j>=0 and i<n and j<m

        def bfs():
            if not q:
                return 0
            r = 0            
            while(q):
                for w in range(len(q)):
                    s = q.popleft()
                    for dx, dy in d:
                        a = s[0]+dx
                        b = s[1]+dy
                        if valid(a, b) and grid[a][b] == 1:
                            q.append([a, b])
                            grid[a][b] = 2
                r += 1
            return r-1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i, j])
        
        ans = bfs()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return ans
        