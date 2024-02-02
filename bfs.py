from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def bfs(self, s):
        visited = [False]*len(self.graph)
        visited[s] = True
        q = deque()
        q.append(s)
        while(q):
            s = q.popleft()
            print(s, end =" ")
            for i in self.graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True 

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.addEdge(3, 4)
g.bfs(2)
