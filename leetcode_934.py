class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        connected = [[0,1], [1,0], [0,-1], [-1,0]] 
        visited = set()

        def valid(r, c):
            return r>=0 and c>=0 and r<n and c<n
        
        def dfs(i, j):
            visited.add((i, j))
            for d in connected:
                a = i+d[0]
                b = j+d[1]
                if valid(a, b) and (a, b) not in visited and grid[a][b]:
                    dfs(a, b)

        def bfs():
            ans = 0
            q = deque(visited)
            while(q):
                for i in range(len(q)):
                    s = q.popleft()
                    for d in connected:
                        a = s[0]+d[0]
                        b = s[1]+d[1]
                        if valid(a, b) and (a, b) not in visited:
                            if grid[a][b]:
                                print(ans)
                                return ans
                            else:
                                visited.add((a, b))
                                q.append([a, b])
                    
                ans += 1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    return bfs() # multisource bfs
