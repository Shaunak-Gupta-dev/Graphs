# Approach1
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def graph(edges):
            g = defaultdict(list)
            for i in edges:
                g[i[0]].append(i[1])
                g[i[1]].append(i[0])
            return g
        g = graph(edges)
        vis = set()
        print(g)
        def helper(s, d, v):
            if s == d:
                return True
            print(s)
            v.add(s)
            for i in g[s]:
                if i not in v and helper(i, d, v):
                    return True
            return False
        return helper(source, destination, vis)    
        