# O(n) time complexity
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        if n==0: return 0
        #countsort
        cs = [0 for _ in range(n+1)]
        for c in citations:
            cs[ min(n,c)] += 1
        h = 0
        for i in range(n,-1,-1):
            h += cs[i]
            if h >= i:
                return i
        return 0 #no index found
