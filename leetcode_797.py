class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        def helper(i, ans):
            if i == n-1:
                res.append(ans+[i])
            for j in graph[i]:
                helper(j, ans+[i])
        helper(0, [])
        return res