class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        inD = defaultdict(int)
        for i in edges:
            inD[i[0]] += 1
            inD[i[1]] += 1
        for i in inD:
            if inD[i] > 1:
                return i
        