from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def dfsH(self, curr, vis):
        print(curr)
        vis.add(curr)
        for i in self.graph[curr]:
            if i not in vis:
                self.dfsH(i, vis)
    def dfs(self, curr):
        visited = set()
        self.dfsH(curr, visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(2)
