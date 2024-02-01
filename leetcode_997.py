class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inD = [0] * (n+1)
        outD = [0] * (n+1)
        for i, j in trust:
            outD[i] += 1
            inD[j] += 1
        for i in range(1, n+1):
            if inD[i] == n-1 and outD[i] == 0:
                return i
        return -1