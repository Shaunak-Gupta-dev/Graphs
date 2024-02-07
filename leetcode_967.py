class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = set()

        def dfs(i, d):
            if d == n:
                res.add(i)
            else:
                w = i%10
                if w+k <= 9:
                    dfs(i*10+w+k, d+1)
                if w-k >= 0:
                    dfs(i*10+w-k, d+1)

        for i in range(1, 10):
            dfs(i, 1)

        return list(res)
        
        
        